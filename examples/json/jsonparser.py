from __future__ import print_function
from bison import BisonParser
import time
import os
import json


class Parser(BisonParser):

    def __init__(self, **kwargs):
        self.bisonEngineLibName = self.__class__.__name__ + '_engine'

        self.options = [
            "%define api.pure full",
            "%define api.push-pull push",
            "%lex-param {yyscan_t scanner}",
            "%parse-param {yyscan_t scanner}",
            "%define api.value.type {void *}",
        ]

        tokens = [[x.strip() for x in y.split('=')]
                  for y in self.__doc__.split('\n')
                  if y.strip() != '']

        self.precedences = ()

        self.start = "value"
        return_location = kwargs.pop('return_location', False)
        if return_location:
            fmt = "{} {{ returntoken_loc({}); }}"
        else:
            fmt = "{} {{ returntoken({}); }}"
        lex_rules = '\n'.join([fmt
                               .format(*x) if x[1][0] != '_' else
                               "{} {{ {} }}".format(x[0], x[1][1:])
                               for x in tokens])

        self.tokens = sorted(list(set([x[1] for x in tokens if not x[1].startswith('_')])))
        self.lexscript = r"""
%option reentrant bison-bridge bison-locations
%{
// Start node is: """ + self.start + r"""
#include "tmp.tab.h"
#include "Python.h"

extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);

PyMODINIT_FUNC PyInit_JSONParser(void) { /* windows needs this function */ }

#define returntoken(tok)                                       \
        *yylval = (void*)PyUnicode_FromString(strdup(yytext)); \
        return tok;
#define YY_INPUT(buf,result,max_size) {                        \
    (*py_input)(py_parser, buf, &result, max_size);            \
}
%}

%%
""" + lex_rules + """

%%

int yywrap(yyscan_t scanner) { return 1; }
    """
        super().__init__(**kwargs)


class JSONParser(Parser):
    r"""
        -?[0-9]+                            = INTEGER
        -?[0-9]+([.][0-9]+)?([eE]-?[0-9]+)? = FLOAT
        false|true|null                     = BOOL
        \"([^\"]|\\[.])*\"                  = STRING
        \{                                  = O_START
        \}                                  = O_END
        \[                                  = A_START
        \]                                  = A_END
        ,                                   = COMMA
        :                                   = COLON
        [ \t\n]                             = _
    """

    @staticmethod
    def on_value(target, option, names, values):
        """
        value
        : string
        | INTEGER
        | FLOAT
        | BOOL
        | array
        | object
        """
        if option == 1:
            return int(values[0])
        if option == 2:
            return float(values[0])
        if option == 3:
            return {'false': False,
                    'true': True,
                    'null': None}[values[0]]
        return values[0]

    @staticmethod
    def on_string(target, option, names, values):
        """
        string
        : STRING
        """
        return values[0][1:-1]

    @staticmethod
    def on_object(target, option, names, values):
        """
        object
        : O_START O_END
        | O_START members O_END
        """
        return {} if option == 0 else dict(values[1])

    @staticmethod
    def on_members(target, option, names, values):
        """
        members
        : pair
        | pair COMMA members
        """
        if option == 0:
            return [values[0]]
        return [values[0]] + values[2]

    @staticmethod
    def on_pair(target, option, names, values):
        """
        pair
        : string COLON value
        """
        return values[0], values[2]

    @staticmethod
    def on_array(target, option, names, values):
        """
        array
        : A_START A_END
        | A_START elements A_END
        """
        if option == 0:
            return ()
        return values[1]

    @staticmethod
    def on_elements(target, option, names, values):
        """
        elements
        : value
        | value COMMA elements
        """
        if option == 0:
            return [values[0]]
        return [values[0]] + values[2]


if __name__ == '__main__':

    start = time.time()
    j = JSONParser(verbose=True, debug=False)
    duration = time.time() - start
    print('instantiate parser', duration)

    file = 'example.json'

    start = time.time()
    with open(file) as fh:
        result_json = json.load(fh)
    duration = time.time() - start
    print('json {}'.format(duration))

    start = time.time()
    result_bison = j.run(file=file, debug=0)
    duration = time.time() - start
    print('bison-based JSONParser {}'.format(duration))
    print('result equal to json: {}'.format(result_json == result_bison))

    print('filesize: {} kB'.format(os.stat(file).st_size / 1024))
