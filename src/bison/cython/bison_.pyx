# cython: language_level=3, linetrace=True
"""
Pyrex-generated portion of pybison
"""
import logging
LOGGER = logging.getLogger(__name__)


cdef extern from "Python.h":
    IF PY3:
        object PyBytes_FromString(char *)
        object PyUnicode_FromString(char *)
        char *PyBytes_AsString(object o)
    ELSE:
        object PyString_FromStringAndSize(char *, int)
        object PyString_FromString(char *)
        char *PyString_AsString(object o)
    object PyInt_FromLong(long ival)
    long PyInt_AsLong(object io)

    object PyList_New(int len)
    int PyList_SetItem(object list, int index, object item)

    void Py_INCREF(object o)

    object PyObject_GetAttrString(object o, char *attr_name)
    object PyTuple_New(int len)
    int PyTuple_SetItem(object p, int pos, object o)
    object PyObject_Call(object callable_object, object args, object kw)
    object PyObject_CallObject(object callable_object, object args)
    int PyObject_SetAttrString(object o, char *attr_name, object v)

# use libdl for now - easy and simple - maybe switch to
# glib or libtool if a keen windows dev sends in a patch

#cdef extern from "dlfcn.h":
#    void *dlopen(char *filename, int mode)
#    int dlclose(void *handle)
#    void *dlsym(void *handle, char *name)
#    char *dlerror()
#
#    ctypedef enum DL_MODES:
#        RTLD_LAZY
#        RTLD_NOW
#        RTLD_BINDING_MASK
#        RTLD_NOLOAD
#        RTLD_GLOBAL

cdef extern from "stdio.h":
    int printf(char *format,...)

cdef extern from "string.h":
    void *memcpy(void *dest, void *src, long n)

# Callback function which is invoked by target handlers
# within the C yyparse() function.
cdef extern from "../c/bison_callback.h":
    object py_callback(object, char *, int, int,...)
    void py_input(object, char *, int *, int)

cdef extern from "../c/bisondynlib.h":
    void *bisondynlib_open(char *filename)
    int bisondynlib_close(void *handle)
    void bisondynlib_reset()
    char *bisondynlib_err()
    object (*bisondynlib_lookup_parser(void *handle))(object, char *)
    char *bisondynlib_lookup_hash(void *handle)
    object bisondynlib_run(void *handle, object parser, void *cb, void *pyin, int debug)

    #int bisondynlib_build(char *libName, char *includedir)


import sys, os, hashlib, re, traceback
import shutil
import distutils.log
import distutils.sysconfig
import distutils.ccompiler
import subprocess
from pathlib import Path
from importlib import machinery
import textwrap

reSpaces = re.compile("\\s+")

unquoted = '[^\'"]%s[^\'"]?'


cdef class ParserEngine:
    """
    Wraps the interface to the binary bison/lex-generated parser engine dynamic
    library.

    You shouldn't need to deal with this at all.

    Takes care of:
        - building the library (if the parser rules have changed)
        - loading the library and extracting the parser entry point
        - calling the entry point
        - closing the library

    Makes direct calls to the platform-dependent routines in
    bisondynlib-[linux|windows].c
    """
    cdef object parser
    cdef object parserHash # hash of current python parser object
    cdef object libFilename_py

    cdef void *libHandle

    # rules hash str embedded in bison parser lib
    cdef char *libHash

    def __init__(self, parser):
        """
        Creates a ParserEngine wrapper, and builds/loads the library.

        Arguments:
            - parser - an instance of a subclass of Parser

        In the course of initialisation, we check the library against the
        parser object's rules. If the lib doesn't exist, or can't be loaded, or
        doesn't match, we build a new library.

        Either way, we end up with a binary parser engine which matches the
        current rules in the parser object.
        """
        self.parser = parser

        self.libFilename_py = parser.buildDirectory \
                              + parser.bisonEngineLibName \
                              + machinery.EXTENSION_SUFFIXES[0]

        self.parserHash = hashParserObject(self.parser)


        if parser._buildOnlyCFiles:
            self.buildLib()
            return
        self.openCurrentLib()

    @staticmethod
    def distutils_dir_name(dname):
        import sysconfig, sys
        """Returns the name of a distutils build directory"""
        f = "{dirname}.{platform}-{version[0]}.{version[1]}"
        return f.format(dirname=dname,
                        platform=sysconfig.get_platform(),
                        version=sys.version_info)

    def reset(self):
        """
        Reset Flex's buffer and state.
        """
        bisondynlib_reset()

    def openCurrentLib(self):
        """
        Tests if library exists and is current. If not, builds a fresh one.

        Opens the library and imports the parser entry point.
        """

        parser = self.parser
        verbose = parser.verbose

        if verbose:
            distutils.log.set_verbosity(1)

        # search for a shared object
        filenames = self.possible_so(parser.buildDirectory)

        self.libFilename_py = ""
        if len(filenames) == 1:
            self.libFilename_py = filenames[0]

        if not os.path.isfile(self.libFilename_py):
            self.buildLib()
            # search for a shared object
            filenames = self.possible_so(parser.buildDirectory)

            self.libFilename_py = ""
            if len(filenames) == 1:
                self.libFilename_py = filenames[0]

        self.openLib()

        # hash parser spec, compare to hash val stored in lib
        IF PY3:
            libHash = PyUnicode_FromString(self.libHash)
        ELSE:
            libHash = PyString_FromString(self.libHash)
        if self.parserHash != libHash:
            if verbose:
                LOGGER.info("Hash discrepancy, need to rebuild bison lib")
                LOGGER.info("  current parser class: %s" % self.parserHash)
                LOGGER.info("         bison library: %s" % libHash)
            self.closeLib()
            self.buildLib()
            self.openLib()
        else:
            if verbose:
                LOGGER.info("Hashes match, no need to rebuild bison engine lib")

    def possible_so(self, so_dir):
        LOGGER.debug("call def possible_so")
        import fnmatch
        regex_str =  '*' + self.parser.bisonEngineLibName + machinery.EXTENSION_SUFFIXES[0]
        return [
            os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(so_dir)
            for f in fnmatch.filter(files, regex_str)
        ]

    def openLib(self):
        """
        Loads the parser engine's dynamic library, and extracts the following
        symbols:

            - void *do_parse() (runs parser)
            - char *parserHash (contains hash of python parser rules)

        Returns lib handle, plus pointer to do_parse() function, as long ints
        (which later need to be cast to pointers)

        Important note -this is totally linux-specific.
        If you want windows support, you'll have to modify these funcs to
        use glib instead (or create windows equivalents), in which case I'd
        greatly appreciate you sending me a patch.
        """
        LOGGER.debug("call def openLib")
        cdef char *libFilename
        cdef char *err
        cdef void *handle

        # convert python filename string to c string
        filename_bytes = self.libFilename_py.encode("ascii")
        # `filename_bytes` has to be its own variable
        # or it gets gc'ed before libFilename is used
        IF PY3:
            libFilename = PyBytes_AsString(filename_bytes)
        ELSE:
            libFilename = PyString_AsString(filename_bytes)

        parser = self.parser

        if parser.verbose:
            LOGGER.info("Opening library {}".format(self.libFilename_py))

        handle = bisondynlib_open(libFilename)
        if handle == NULL:
            raise Exception('library loading failed!')
        self.libHandle = handle

        err = bisondynlib_err()
        if err:
            LOGGER.error('ParserEngine.openLib: error "{}"\n'.format(err))
            return

        # extract symbols
        self.libHash = bisondynlib_lookup_hash(handle)

        if parser.verbose:
            LOGGER.info("Successfully loaded library")

    def generate_exception_handler(self):
        LOGGER.debug("call generate_exception_handler")
        s = '''
            {
                PyObject* obj = PyErr_Occurred();
                if (obj) {
                      // yyerror(&yylloc, "exception raised");
                      YYERROR;
                }
            }'''
        return s

    def buildLib(self):
        """
        Creates the parser engine lib

        This consists of:
            1. Ripping the tokens list, precedences, start target, handler docstrings
               and lex script from this Parser instance's attribs and methods
            2. Creating bison and lex files
            3. Compiling bison/lex files to C
            4. Compiling the C files, and link into a dynamic lib
        """
        LOGGER.debug("call def buildLib")
        # -------------------------------------------------
        # rip the pertinent grammar specs from parser class
        parser = self.parser

        # get target handler methods, in the order of appearance in the
        # source file.
        attribs = dir(parser)
        gHandlers = []

        for a in attribs:
            if a.startswith('on_'):
                method = getattr(parser, a)
                gHandlers.append(method)

        gHandlers.sort(key=keyLines)

        # get start symbol, tokens, precedences, lex script
        gOptions = parser.options
        gStart = parser.start
        gTokens = parser.tokens
        gPrecedences = parser.precedences
        gLex = parser.lexscript

        buildDirectory = parser.buildDirectory

        # ------------------------------------------------
        # now, can generate the grammar file
        if os.path.isfile(buildDirectory + parser.bisonFile):
            os.unlink(buildDirectory + parser.bisonFile)

        if parser.verbose:
            LOGGER.debug("generating bison file: {}".format(buildDirectory + parser.bisonFile))

        f = open(buildDirectory + parser.bisonFile, "w")
        write = f.write
        #writelines = f.writelines
        if sys.platform == "win32":
            export = "__declspec(dllexport) "
        else:
            export = "__attribute__ ((dllexport)) "


        # define yyerror for reentrant/nonreentrant parser
        if "%define api.pure full" in gOptions:
            error_def = 'void yyerror(YYLTYPE *locp, yyscan_t scanner, char const *msg);'
        else:
            error_def = 'int yyerror(char *msg);'


        # grammar file prologue
        write('\n'.join([
            '%code top {',
            '',
            '#include "tmp.tab.h"',
            '#include "lex.yy.h"',
            '#include "Python.h"',
            # '' if sys.platform == 'win32' else 'extern int yylineno;'
            # '#define YYSTYPE void*',
            #'extern void *py_callback(void *, char *, int, void*, ...);',
            'void *(*py_callback)(void *, char *, int, int, ...);',
            'void (*py_input)(void *, char *, int *, int);',
            'void *py_parser;',
            export + 'char *rules_hash = "%s";' % self.parserHash,
            '#define YYERROR_VERBOSE 1',
            '',
            '}',
            '',
            '%code requires {',
            '',
            'typedef void * yyscan_t;',
            '#define YYLTYPE YYLTYPE',
            'typedef struct YYLTYPE',
            '{',
            '  int first_line;',
            '  int first_column;',
            '  int last_line;',
            '  int last_column;',
            '  char *filename;',
            '} YYLTYPE;',
            #'',
            #'YYLTYPE yylloc; /* location data */'
            '',
            error_def,
            '}',
            '',
            '%locations',
            '',
            ]))

        # write out tokens and start target dec
        write('%%token %s\n\n' % ' '.join(gTokens))
        write('%%start %s\n\n' % gStart)
        write("\n".join(["%s" % d for d in gOptions]))

        # write out precedences
        for p in gPrecedences:
            write("%%%s  %s\n" % (p[0], " ".join(p[1])))

        write("\n\n%%\n\n")

        if parser.raw_c_rules:
            write(parser.raw_c_rules)

        # carve up docstrings
        rules = []
        for h in gHandlers:

            doc = h.__doc__.strip()

            # added by Eugene Oden
            #target, options = doc.split(":")
            doc = re.sub(unquoted % ";", "", doc)

            s = re.split(unquoted % ":", doc)

            target, options = s
            target = target.strip()

            options = options.strip()
            tmp = []

            #opts = options.split("|")
            r = unquoted % r"\|"
            opts1 = re.split(r, " " + options)

            for o in opts1:
                o = o.strip()

                tmp.append(reSpaces.split(o))
            options = tmp

            rules.append((target, options))

        # and render rules to grammar file
        for rule in rules:
            try:
                write("%s\n    : " % rule[0])
                options = []
                idx = 0
                for option in rule[1]:
                    nterms = len(option)
                    if nterms == 1 and option[0] == '':
                        nterms = 0
                        option = []
                    action = '\n        {\n'
                    if 'error' in option:
                        action = action + "             yyerrok;\n"
                        action = action + "             PyObject* lasterr = PyObject_GetAttrString((PyObject*)py_parser, \"lasterror\");;\n"
                    action = action + '          $$ = (*py_callback)(\n            py_parser, "%s", %s, %%s' % \
                                      (rule[0], idx) # note we're deferring the substitution of 'nterms' (last arg)
                    args = []
                    i = -1

                    if nterms == 0:
                        args.append('NULL')
                    else:
                        for i in range(nterms):
                            if option[i] == '%prec':
                                i = i - 1
                                break # hack for rules using '%prec'
                            o = option[i].replace('"', '\\"')
                            if o == 'error':
                                args.append('"%s", lasterr' % (o))
                            else:
                                args.append('"%s", $%d' % (o, i+1))

                    # now, we have the correct terms count
                    action = action % (i + 1)

                    # assemble the full rule + action, add to list
                    action = action + ",\n            "
                    action = action + ",\n            ".join(args) + "\n            );\n"

                    if 'error' in option:
                        action = action + " PyObject_SetAttrString(py_parser, \"lasterror\", Py_None);\n"
                        action = action + "             Py_DECREF(lasterr);\n"
                        action = action + "             Py_INCREF(Py_None);\n"
                        action = action + "             yyclearin;\n"

                    else:
                        action = action + self.generate_exception_handler()

                    action = action + '        }\n'

                    options.append(" ".join(option) + action)
                    idx = idx + 1
                write("    | ".join(options) + "    ;\n\n")
            except:
                traceback.print_exc()

        write('\n\n%%\n\n')

        # now generate C code
        epilogue = '\n'.join([
            export + 'void do_parse(void *parser1,',
            '              void *(*cb)(void *, char *, int, int, ...),',
            '              void (*in)(void *, char*, int *, int),',
            '              int debug',
            '              )',
            '{',
            '   py_callback = cb;',
            '   py_input = in;',
            '   py_parser = parser1;',
            '   yydebug = debug; // For Bison (still global, even in a reentrant parser)',
            '',
        ])

        if "%define api.pure full" in gOptions:
            epilogue += '\n'.join([
                'yyscan_t scanner;',
                'yylex_init(&scanner);',

                'if (debug) yyset_debug(1, scanner); // For Flex (no longer a global, but rather a member of yyguts_t)',
                '',
                '',
                'int status;',
                'yypstate *ps = yypstate_new ();',
                'YYSTYPE pushed_value;',
                'YYLTYPE yylloc;',
                'yylloc.first_line = yylloc.first_column = yylloc.last_line = yylloc.last_column = 1;',
                'do {',
                '  int token = yylex(&pushed_value,&yylloc, scanner);',
                '  status = yypush_parse (ps, token , &pushed_value, &yylloc, scanner);',
                '} while (status == YYPUSH_MORE);',
                'yypstate_delete(ps);',
                'yylex_destroy(scanner);'
                'return;',
            '}',
            '',
            '',
            'void yyerror(YYLTYPE *locp, yyscan_t scanner, char const *msg) {',
            '',
            '  PyObject *error = PyErr_Occurred();',
            '  if(error) PyErr_Clear();',
            '  PyObject *fn = PyObject_GetAttrString((PyObject *)py_parser,',
            '                                        "report_syntax_error");',
            '  if (!fn)',
            '      return;',
            '',
            '  PyObject *args;',
            '  args = Py_BuildValue("(s,s,i,i,i,i)", msg, yyget_text(scanner),',
            '                       locp->first_line, locp->first_column,',
            '                       locp->last_line, locp->last_column);',
            '',
            '  if (!args)',
            '      return;',
            '',
            # '  fprintf(stderr, "%d.%d-%d.%d: error: \'%s\' before \'%s\'.",',
            # '          locp->first_line, locp->first_column,',
            # '          locp->last_line, locp->last_column, msg, yyget_text(scanner));',
            '',
            '  PyObject *res = PyObject_CallObject(fn, args);',
            '  Py_DECREF(args);',
            #'  Py_DECREF(fn);',
            '',
            '  if (!res)',
            '      return;',
            '',
            '  Py_XDECREF(res);',
            '  return;',
            '}',
            ]) + '\n'

        else:
            epilogue += '\n'.join([
            '   yyparse();',
            '}',
            '',
            # 'extern char *yytext;',
            '',
            'int yyerror(char *msg)',
            '{',
            '  PyObject *error = PyErr_Occurred();',
            '  if(error) PyErr_Clear();',
            '  PyObject *fn = PyObject_GetAttrString((PyObject *)py_parser,',
            '                                        "report_syntax_error");',
            '  if (!fn)',
            '      return 1;',
            '',
            '  PyObject *args;',
            '  args = Py_BuildValue("(s,s,i,i,i,i)", msg, yytext,',
            '                       yylloc.first_line, yylloc.first_column,',
            '                       yylloc.last_line, yylloc.last_column);',
            '',
            '  if (!args)',
            '      return 1;',
            #'',
            #'  fprintf(stderr, "%d.%d-%d.%d: error: \'%s\' before \'%s\'.",',
            #'          yylloc.first_line, yylloc.first_column,',
            #'          yylloc.last_line, yylloc.last_column, msg, yytext);',
            '',
            '  PyObject *res = PyObject_CallObject(fn, args);',
            '  Py_DECREF(args);',
            '',
            '  if (!res)',
            '      return 1;',
            '',
            '  Py_XDECREF(res);',
            '  return 0;',
            '}',
            ]) + '\n'
        write(epilogue)

        # done with grammar file
        f.close()

        # -----------------------------------------------
        # now generate the lex script
        if os.path.isfile(buildDirectory + parser.flexFile):
            os.unlink(buildDirectory + parser.flexFile)

        f = open(buildDirectory + parser.flexFile, 'w')
        f.write(textwrap.dedent(gLex))
        f.close()

        # create and set up a compiler object
        if sys.platform == 'win32':
            env = distutils.ccompiler.new_compiler(verbose=parser.verbose)
            env.initialize()
            env.add_library('python{v.major}{v.minor}'.format(v=sys.version_info))
            env.add_include_dir(distutils.sysconfig.get_python_inc())
            env.add_library_dir(os.path.join(sys.prefix, 'libs'))
        else:
            env = distutils.ccompiler.new_compiler(verbose=parser.verbose)
            env.add_include_dir(distutils.sysconfig.get_python_inc())
            env.define_macro('__declspec(x)')

        # gather possible include directories from lexscript
        included_files = [
            l for l in
            [l.replace("#include ", "").split("//")[0].replace("<","").replace(">", "").replace('"', '')
             for l in parser.lexscript.strip().split("\n")
             if l.strip().startswith("#include")]
            if Path(l).exists()
        ]

        if parser.verbose:
            LOGGER.info("Included files needed: {}".format(";".join(included_files)))

        for inc_f in included_files:
            if parser.verbose:
                LOGGER.info("Copying file {} => {}".format(inc_f, buildDirectory + inc_f))
            shutil.copy(inc_f, buildDirectory + inc_f)

        # --------------------------------- #
        # Now run bison on the grammar file #
        # --------------------------------- #
        bisonCmd = parser.bisonCmd + [buildDirectory + parser.bisonFile]

        if parser.verbose:
            LOGGER.info("bison cmd: {}".format(' '.join(bisonCmd)))

        # env.spawn(bisonCmd)
        proc = subprocess.Popen(' '.join(bisonCmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if proc.returncode:
            raise Exception(err)

        if parser.verbose:
            LOGGER.info("CMD Output: {}".format(out))

        if parser.verbose:
            LOGGER.info("renaming bison output files")
            LOGGER.info("{} => {}{}".format(parser.bisonCFile, buildDirectory,
                                      parser.bisonCFile1))
            LOGGER.info("{} => {}{}".format(parser.bisonHFile, buildDirectory,
                                      parser.bisonHFile1))

        if os.path.isfile(buildDirectory + parser.bisonCFile1):
            os.unlink(buildDirectory + parser.bisonCFile1)

        shutil.copy(parser.bisonCFile, buildDirectory + parser.bisonCFile1)
        # delete 'local' file
        os.remove(parser.bisonCFile)

        if os.path.isfile(buildDirectory + parser.bisonHFile1):
            os.unlink(buildDirectory + parser.bisonHFile1)

        shutil.copy(parser.bisonHFile, buildDirectory + parser.bisonHFile1)
        # delete 'local' file
        os.remove(parser.bisonHFile)

        # -----------------------------------------
        # Now run lex on the lex file
        #os.system('lex tmp.l')
        flexCmd = parser.flexCmd + [buildDirectory + parser.flexFile]

        if parser.verbose:
            LOGGER.info("flex cmd: {}".format(' '.join(flexCmd)))

        # env.spawn(flexCmd)
        proc = subprocess.Popen(' '.join(flexCmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if proc.returncode:
            raise Exception(err)

        if parser.verbose:
            LOGGER.info("CMD Output: {}".format(out))

        if os.path.isfile(buildDirectory + parser.flexCFile1):
            os.unlink(buildDirectory + parser.flexCFile1)
        if parser.verbose:
            LOGGER.info("{} => {}{}".format(parser.flexCFile, buildDirectory, parser.flexCFile1))
        shutil.copy(parser.flexCFile, buildDirectory + parser.flexCFile1)
        # delete 'local' file
        os.remove(parser.flexCFile)

        if os.path.isfile(buildDirectory + parser.flexHFile1):
            os.unlink(buildDirectory + parser.flexHFile1)
        if parser.verbose:
            LOGGER.info("{} => {}{}".format(parser.flexHFile, buildDirectory, parser.flexHFile1))
        shutil.copy(parser.flexHFile, buildDirectory + parser.flexHFile1)
        # delete 'local' file
        # os.remove(parser.flexHFile)


        if parser._buildOnlyCFiles:
            return

        libFileName = buildDirectory + parser.bisonEngineLibName \
                      + machinery.EXTENSION_SUFFIXES[0]

        if parser.verbose:
            LOGGER.info("Compiling: {}".format(libFileName))
        # -----------------------------------------
        # Now compile the files into a shared lib
        objs = env.compile([buildDirectory + parser.bisonCFile1,
                            buildDirectory + parser.flexCFile1],
                           extra_preargs=parser.cflags_pre,
                           extra_postargs=parser.cflags_post,
                           debug=parser.debugSymbols)

        if os.path.isfile(libFileName+".bak"):
            os.unlink(libFileName+".bak")

        if os.path.isfile(libFileName):
            os.rename(libFileName, libFileName+".bak")

        if parser.verbose:
            LOGGER.info("linking: {} => {}".format(', '.join(objs), libFileName))

        if sys.platform.startswith("darwin"):
            # on OSX, ld throws undefined symbol for shared library references
            # however, we would like to link against libpython dynamically, so that
            # the built .so will not depend on which python interpreter it runs on
            env.linker_so += ["-undefined", "dynamic_lookup"]

        # link 'em into a shared lib
        env.link_shared_object(objs, libFileName)

        #cdef char *incdir
        #incdir = PyString_AsString(get_python_inc())
        #bisondynlib_build(self.libFilename_py, incdir)

        # --------------------------------------------
        # clean up, if we succeeded
        # hitlist = objs[:]
        hitlist = []

        if os.path.isfile(self.libFilename_py):
            for name in ['bisonFile', 'bisonCFile', 'bisonHFile',
                         'bisonCFile1', 'bisonHFile1', 'flexFile',
                         'flexCFile', 'flexCFile1',
                         ] + objs:
                if hasattr(parser, name):
                    fname = buildDirectory + getattr(parser, name)
                else:
                    fname = None
                if fname and os.path.isfile(fname):
                    hitlist.append(fname)

        if not parser.keepfiles:
            for f in hitlist:
                try:
                    os.remove(f)
                except:
                    LOGGER.warning("failed to delete temporary file {}".format(f))

            if parser.verbose:
                LOGGER.info("Deleting temporary bison output files:")

            for f in [parser.bisonCFile, parser.bisonHFile, parser.flexCFile, "tmp.output"]:
                if os.path.isfile(f):
                    if parser.verbose:
                        LOGGER.info('rm {}'.format(f))
                    os.remove(f)

    def closeLib(self):
        """
        Does the necessary cleanups and closes the parser library
        """
        LOGGER.debug("call def closeLib")
        bisondynlib_close(self.libHandle)

    def runEngine(self, debug=0):
        """
        Runs the binary parser engine, as loaded from the lib
        """
        LOGGER.debug("call def runEngine")
        cdef void *handle

        cdef void *cbvoid
        cdef void *invoid

        handle = self.libHandle
        parser = self.parser

        cbvoid = <void *>py_callback
        invoid = <void *>py_input

        try:
            ret = bisondynlib_run(handle, parser, cbvoid, invoid, debug)
        except Exception as e:
            ret=None

        return ret

    def __del__(self):
        """
        Clean up and bail
        """
        LOGGER.debug("call __del__")
        self.closeLib()


def cmpLines(meth1, meth2):
    """
    Used as a sort() argument for sorting parse target handler methods by
    the order of their declaration in their source file.
    """
    try:
        line1 = meth1.__code__.co_firstlineno
        line2 = meth2.__code__.co_firstlineno
    except:
        line1 = meth1.__init__.__code__.co_firstlineno
        line2 = meth2.__init__.__code__.co_firstlineno

    return (line1 > line2) - (line1 < line2)

def keyLines(meth):
    """
    Used as a sort() 'key' argument for sorting parse target handler methods by
    the order of their declaration in their source file.
    """
    try:
        line = meth.__code__.co_firstlineno
    except:
        line = meth.__init__.__code__.co_firstlineno

    return line


def hashParserObject(parser):
    """
    Calculates an sha1 hex 'hash' of the lex script
    and grammar rules in a parser class instance.

    This is based on the raw text of the lex script attribute,
    and the grammar rule docstrings within the handler methods.

    Used to detect if someone has changed any grammar rules or
    lex script, and therefore, whether a shared parser lib rebuild
    is required.
    """
    hasher = hashlib.new('sha1')

    def update(o):
        if type(o) == type(""):
            o=o.encode("utf-8")
        hasher.update(o)

    # add the lex script
    update(parser.lexscript)

    # add the tokens
    # workaround pyrex weirdness
    # tokens = list(parser.tokens)
    tokens = parser.tokens[0]
    update(",".join(tokens))

    # add the precedences
    for direction, tokens in parser.precedences:
        tokens = tokens[0]
        update(direction + "".join(tokens))

    # extract the parser target handler names
    handlerNames = dir(parser)

    #handlerNames = filter(lambda m: m.startswith('on_'), dir(parser))
    tmp = []
    for name in handlerNames:
        if name.startswith('on_'):
            tmp.append(name)
    handlerNames = tmp
    handlerNames.sort()

    # extract method objects, filter down to callables
    #handlers = [getattr(parser, m) for m in handlerNames]
    #handlers = filter(lambda h: callable(h), handlers)
    tmp = []
    for m in handlerNames:
        attr = getattr(parser, m)
        if callable(attr):
            tmp.append(attr)
    handlers = tmp

    # now add in the methods' docstrings
    for h in handlers:
        docString = h.__doc__
        update(docString)

    # done
    return hasher.hexdigest()
