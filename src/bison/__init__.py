"""
Wrapper module for interfacing with Bison (yacc)

Written April 2004 by David McNab <david@freenet.org.nz>
Copyright (c) 2004 by David McNab, all rights reserved.

Released under the GNU General Public License, a copy of which should appear in
this distribution in the file called 'COPYING'. If this file is missing, then
you can obtain a copy of the GPL license document from the GNU website at
http://www.gnu.org.

This software is released with no warranty whatsoever. Use it at your own
risk.

If you wish to use this software in a commercial application, and wish to
depart from the GPL licensing requirements, please contact the author and apply
for a commercial license.
"""

from __future__ import absolute_import
from __future__ import print_function

import shutil
from os.path import dirname, join

import sys
import os
import traceback
try:
    from io import BytesIO as IO
except:
    from cStringIO import StringIO as IO

from os import makedirs

from .bison_ import ParserEngine
from .node import BisonNode
from .convert import bisonToPython

WIN_FLEX = join(dirname(__file__),
                'winflexbison', 'win_flex.exe')
WIN_BISON = join(dirname(__file__),
                 'winflexbison', 'win_bison.exe')


class BisonSyntaxError(Exception):
    def __init__(self, msg, args=[]):
        super(BisonSyntaxError, self).__init__(msg)

        if args:
            self.first_line, self.first_col, self.last_line, self.last_col, \
                    self.message, self.token_value = args


class TimeoutError(Exception):
    pass


class BisonParser(object):
    """
    Base parser class

    You should subclass this, and provide a bunch of methods called
    'on_TargetName', where 'TargetName' is the name of each target in
    your grammar (.y) file.
    """
    # ---------------------------------------
    # override these if you need to

    raw_c_rules = ''

    # Command and options for running yacc/bison, except for filename arg
    bisonCmd = []
    if sys.platform == 'win32':
        bisonCmd = [WIN_BISON, '-d', '-v', '-t']
    else:
        bisonCmd.append('bison')
        bisonCmd = ['bison', '-d', '-v', '-t']

    bisonFile = 'tmp.y'
    bisonCFile = 'tmp.tab.c'

    # Name of header file generated by bison cmd.
    bisonHFile = 'tmp.tab.h'

    # C output file from bison gets renamed to this.
    bisonCFile1 = 'tmp.bison.c'

    # Bison-generated header file gets renamed to this.
    bisonHFile1 = 'tokens.h'

    # command and options for running [f]lex, except for filename arg.
    flexCmd = []
    if sys.platform == 'win32':
        # flexCmd.append('-DYY_NO_UNISTD_H=false')
        flexCmd = [WIN_FLEX, '--wincompat']
    else:
        flexCmd = ['flex']

    flexFile = 'tmp.l'
    flexCFile = 'lex.yy.c'

    # C output file from flex gets renamed to this.
    flexCFile1 = 'tmp.lex.c'

    # CFLAGS added before all command line arguments.
    cflags_pre = ['-fPIC'] if sys.platform.startswith('linux') else []

    # CFLAGS added after all command line arguments.
    cflags_post = ['-O3', '-g'] if sys.platform.startswith('linux') else []

    # Directory used to store the generated / compiled files.
    buildDirectory = ''

    # Add debugging symbols to the binary files.
    debugSymbols = 1

    # Enable verbose debug message sent to stdout.
    verbose = 0

    # Timeout in seconds after which the parser is terminated.
    # TODO: this is currently not implemented.
    timeout = 1

    # Default to sys.stdin.
    file = None

    # Create a marker for input parsing.
    marker = 0

    # Last parsed target, top of parse tree.
    last = None

    # Enable this to keep all temporary engine build files.
    keepfiles = 1

    # Prefix of the shared object / dll file. Defaults to 'modulename-engine'.
    # If the module is executed directly, "__main__" will be used (since that
    # that is the "module name", in that case).
    bisonEngineLibName = None

    # Class to use by default for creating new parse nodes. If set to None,
    # BisonNode will be used.
    default_node_class = BisonNode

    error_threshold = 10

    def __init__(self, **kw):
        """
        Abstract representation of parser

        Keyword arguments:
            - read - a callable accepting an int arg (nbytes) and returning a string,
              default is this class' read() method
            - file - a file object, or string of a pathname to open as a file, defaults
              to sys.stdin. Note that you can leave this blank, and pass a file keyword
              argument to the .run() method.
            - verbose - set to 1 to enable verbose output messages, default 0
            - keepfiles - if non-zero, keeps any files generated in the
              course of building the parser engine; by default, all these
              files get deleted upon a successful engine build
            - defaultNodeClass - the class to use for creating parse nodes, default
              is self.defaultNodeClass (in this base class, BisonNode)
        """
        self.debug = kw.get('debug', 0)

        self.buildDirectory = '/tmp/pybison/pybison_' + type(self).__name__ + os.path.sep
        if self.debug:
            shutil.rmtree(self.buildDirectory, ignore_errors=True)
        makedirs(self.buildDirectory, exist_ok=True)

        # setup
        read = kw.get('read', None)
        if read:
            self.read = read

        fileobj = kw.get('file', None)
        if fileobj:
            if isinstance(fileobj, str):
                try:
                    fileobj = open(fileobj, 'rb')
                except:
                    raise Exception('Cannot open input file %s' % fileobj)
            self.file = fileobj
        else:
            self.file = sys.stdin

        nodeClass = kw.get('defaultNodeClass', BisonNode)
        if nodeClass:
            self.defaultNodeClass = nodeClass

        self.verbose = kw.get('verbose', False)
        if self.verbose:
            self.bisonCmd.append('--verbose')

        self.interactive = kw.get('interactive', False)
        self.debugSymbols = kw.get('debugSymbols', False)

        if 'keepfiles' in kw:
            self.keepfiles = kw['keepfiles']

        # if engine lib name not declared, invent ont
        if not self.bisonEngineLibName:
            self.bisonEngineLibName = self.__class__.__module__.split('.')[-1] + '_parser'

        # get an engine
        self.engine = ParserEngine(self)

        self.BisonSyntaxError = BisonSyntaxError

    def __getitem__(self, idx):
        return self.last[idx]

    def _handle(self, targetname, option, names, values):
        """
        Callback which receives a target from parser, as a targetname
        and list of term names and values.

        Tries to dispatch to on_TargetName() methods if they exist,
        otherwise wraps the target in a BisonNode object
        """
        handler = getattr(self, 'on_' + targetname, None)

        if handler:
            if self.verbose:
                try:
                    hdlrline = handler.__code__.co_firstlineno
                except:
                    hdlrline = handler.__init__.__code__.co_firstlineno

                print("BisonParser._handle: call handler at line {} with: {}".format(
                    hdlrline, str((targetname, option, names, values)))
                )
            try:
                self.last = handler(target=targetname, option=option, names=names,
                                    values=values)
            except Exception as e:
                #print("returning exception", e, targetname, option, names, values)
                self.last = e
                return e

            # if self.verbose:
            #    print("handler for {} returned {}".format(targetname, repr(self.last)))
        else:
            if self.verbose:
                print("no handler for {}, using default".format(targetname))

            cls = self.default_node_class
            self.last = cls(target=targetname, option=option, names=names,
                            values=values)

        # assumedly the last thing parsed is at the top of the tree
        return self.last

    def handle_timeout(self, signum, frame):
        raise TimeoutError("Computation exceeded timeout limit.")

    def reset(self):
        self.marker = 0
        self.engine.reset()

    def parse_string(self, string):
        """Supply file-like object containing the string."""
        file = IO(string.encode('utf-8'))
        return self.run(file=file)

    def parse_file(self, filename):
        """Better interface."""
        return self.run(file=filename)

    def run(self, **kw):
        """
        Runs the parser, and returns the top-most parse target.

        Keywords:
            - file - either a string, comprising a file to open and read input from, or
              a Python file object
            - debug - enables garrulous parser debugging output, default 0
        """
        if self.verbose:
            print('Parser.run: calling engine')

        filename = None
        # grab keywords
        i_opened_a_file = False
        fileobj = kw.get('file', self.file)
        if isinstance(fileobj, str):
            filename = fileobj
            try:
                fileobj = open(fileobj, 'rb')
                i_opened_a_file = True
            except:
                raise Exception('Cannot open input file "%s"' % fileobj)
        elif hasattr(fileobj, 'read') and hasattr(fileobj, 'closed'):  # allow BytesIO
            # TODO: Implement BytesIO
            pass
        else:
            filename = None
            fileobj = None

        read = kw.get('read', self.read)

        debug = kw.get('debug', False)

        # back up existing attribs
        oldfile = self.file
        oldread = self.read

        # plug in new ones, if given
        if fileobj:
            self.file = fileobj
        if read:
            self.read = read


        if self.verbose and self.marker:
            print('Parser.run(): self.marker (', self.marker, ') is set')
        if self.verbose and self.file and self.file.closed:
            print('Parser.run(): self.file', self.file, 'is closed')

        error_count = 0
        self.last = None

        # TODO: add option to fail on first error.
        while not self.marker:
            # do the parsing job, spew if error
            self.engine.reset()

            try:
                self.engine.runEngine(debug)
            except Exception as e:
                error_count += 1

                if error_count > self.error_threshold:
                    raise

                self.report_last_error(filename, e)

            if self.verbose:
                print('Parser.run: back from engine')

            if hasattr(self, 'hook_run'):
                self.last = self.hook_run(filename, self.last)

            if self.verbose and not self.marker:
                print('last:', self.last)

        if self.verbose:
            print('last:', self.last)

        # restore old values
        self.file = oldfile
        self.read = oldread
        self.marker = 0

        if self.verbose:
            print('------------------ result=', self.last)

        # close the file if we opened one
        if i_opened_a_file and fileobj:
            fileobj.close()

        # TODO: return last result (see while loop):
        # return self.last[:-1]
        return self.last

    def read(self, nbytes):
        """
        Override this in your subclass, if you desire.

        Arguments:
            - nbytes - the maximum length of the string which you may return.
              DO NOT return a string longer than this, or else Bad Things will
              happen.
        """
        # default to stdin
        if self.verbose:
            print('Parser.read: want %s bytes' % nbytes)

        _bytes = self.file.readline(nbytes)

        if self.verbose:
            print('Parser.read: got %s bytes' % len(_bytes))
            print(_bytes)

        return _bytes

    def report_last_error(self, filename, error):
        """
        Report a raised exception. Depending on the mode in which the parser is
        running, it will:

         - write a verbose message to stderr (verbose=True; interactive=True).
           The written error message will include the type, value and traceback
           of the raised exception.

         - write a minimal message to stderr (verbose=False; interactive=True).
           The written error message will only include the type and value of
           the raised exception.

        """

        # if filename != None:
        #     msg = '%s:%d: "%s" near "%s"' \
        #             % ((filename,) + error)

        #     if not self.interactive:
        #         raise BisonSyntaxError(msg)

        #     print >>sys.stderr, msg
        # elif hasattr(error, '__getitem__') and isinstance(error[0], int):
        #     msg = 'Line %d: "%s" near "%s"' % error

        #     if not self.interactive:
        #         raise BisonSyntaxError(msg)

        #    print >>sys.stderr, msg
        # else:
        if not self.interactive:
            raise

        if self.verbose:
            traceback.print_exc()

        print('ERROR:', error)

    def report_syntax_error(self, msg, yytext, first_line, first_col, last_line, last_col):

        def color_white(txt):
            return "\033[39m" + txt

        def color_red(txt):
            return "\033[31m" + txt

        def color_blue(txt):
            return "\033[34m" + txt

        def make_bold(txt):
            return "\033[1m" + txt

        def reset_style(txt):
            return "\033[0m" + txt

        yytext = yytext.replace('\n', '\\n')
        args = (msg, yytext, first_line, first_col, last_line, last_col)
        err_msg = ''.join([
            color_red(make_bold("Error: ")), reset_style("%s"), "\n", "\t ",
            color_blue("└ near "), make_bold('"%s"'),
            reset_style(color_blue(" (see ")),
            color_white(make_bold("line %d, pos %d to line %d, pos %d")),
            reset_style(color_blue(").")), reset_style('')
        ])
        self.lasterror = msg, yytext, first_line, first_col, last_line, last_col
        raise BisonSyntaxError(err_msg % args, list(args))

    def setSyntaxErrorReporting(self, fn):
        self.report_syntax_error = fn
