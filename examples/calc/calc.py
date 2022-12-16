#!/usr/bin/env python
"""
A simple pybison parser program implementing a calculator
"""
from __future__ import absolute_import
from __future__ import print_function
from bison import BisonParser
from six.moves import input


class Parser(BisonParser):
    """
    Implements the calculator parser. Grammar rules are defined in the method
    docstrings. Scanner rules are in the 'lexscript' attribute.
    """
    options = [
        "%define api.pure full",
        "%define api.push-pull push",
        "%lex-param {yyscan_t scanner}",
        "%parse-param {yyscan_t scanner}",
        "%define api.value.type {void *}",
    ]

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = [
        'NUMBER',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
        'LPAREN', 'RPAREN',
        'NEWLINE', 'QUIT'
    ]

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        ('left', ('MINUS', 'PLUS')),
        ('left', ('TIMES', 'DIVIDE')),
        ('left', ('NEG', )),
        ('right', ('POW', )),
    )

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    # Declare the start target here (by name)
    start = "input"

    def on_input(self, target, option, names, values):
        """
        input :
              | input line
        """
        return

    def on_line(self, target, option, names, values):
        """
        line : NEWLINE
             | exp NEWLINE
        """
        if option == 1:
            print(values[0])

    def on_exp(self, target, option, names, values):
        """
        exp : NUMBER
            | exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp DIVIDE exp
            | MINUS exp %prec NEG
            | exp POW exp
            | LPAREN exp RPAREN
        """
        if option == 0:
            return float(values[0])
        elif option == 1:
            return values[0] + values[2]
        elif option == 2:
            return values[0] - values[2]
        elif option == 3:
            return values[0] * values[2]
        elif option == 4:
            return values[0] / values[2]
        elif option == 5:
            return - values[1]
        elif option == 6:
            return values[0] ** values[2]
        elif option == 7:
            return values[1]

    # -----------------------------------------
    # raw lex script, verbatim here
    # -----------------------------------------
    lexscript = r"""
    %option reentrant bison-bridge bison-locations
    %{
    #include "Python.h"
    #include "tmp.tab.h"
    extern void *py_parser;
    extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
    PyMODINIT_FUNC PyInit_Parser(void) { /* windows needs this function */ }
    #define returntoken(tok) \
            *yylval = (void*)PyUnicode_FromString(strdup(yytext)); return (tok);
    #define YY_INPUT(buf,result,max_size) { \
        (*py_input)(py_parser, buf, &result, max_size); \
    }
    %}

    %%

    [0-9]+ { returntoken(NUMBER); }
    "("    { returntoken(LPAREN); }
    ")"    { returntoken(RPAREN); }
    "+"    { returntoken(PLUS); }
    "-"    { returntoken(MINUS); }
    "*"    { returntoken(TIMES); }
    "**"   { returntoken(POW); }
    "/"    { returntoken(DIVIDE); }
    "quit" { printf("lex: got QUIT\n"); yyterminate(); returntoken(QUIT); }

    [ \t\v\f] {}
    [\n]   { returntoken(NEWLINE); }
    .      { printf("unknown char %c ignored, yytext=0x%lx\n", yytext[0],
                    yytext); /* ignore bad chars */}

    %%

    int yywrap(yyscan_t scanner) { return(1); }
    """


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="PyBison CALC Example")
    parser.add_argument("-k", "--keepfiles", action="store_true",
                        help="Keep temporary files used in building parse engine lib")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose messages while parser is running")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable garrulous debug messages from parser engine")
    args = parser.parse_args()

    p = Parser(keepfiles=args.keepfiles, verbose=args.verbose)

    while True:
        try:
            s = input()
            r = p.parse_string(s, debug=args.debug)
            print(r)
        except (KeyboardInterrupt, EOFError):
            break
