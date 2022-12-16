#!/usr/bin/env python
"""
A more advanced calculator example, with variable storage and scientific
functions (courtesy of python 'math' module)
"""
import math
import sys

from bison import BisonParser
from six.moves import input


class Parser(BisonParser):
    """
    Implements the calculator parser. Grammar rules are defined in the method docstrings.
    Scanner rules are in the 'lexscript' attribute.
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
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'POW',
        'LPAREN', 'RPAREN',
        'NEWLINE', 'QUIT',
        'EQUALS', 'PI', 'E',
        'IDENTIFIER',
        'HELP'
    ]
    
    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        ('left', ('MINUS', 'PLUS')),
        ('left', ('TIMES', 'DIVIDE', 'MOD')),
        ('left', ('NEG', )),
        ('right', ('POW', )),
    )
    
    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = "calc1-engine"

    vars = {}

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
        if option == 1:
            return values[0]

    def on_line(self, target, option, names, values):
        """
        line : NEWLINE
             | exp NEWLINE
             | IDENTIFIER EQUALS exp
             | HELP
             | myquit
        """
        if option == 1:
            print(values[0])
            return values[0]
        elif option == 2:
            self.vars[values[0]] = values[2]
            return values[2]
        elif option == 3:
            self.show_help()

    def on_exp(self, target, option, names, values):
        """
        exp : number | plusexp | minusexp | timesexp | divexp       | modexp
            | negexp | powexp  | parenexp | varexp   | functioncall | constant
        """
        return values[0]

    def on_number(self, target, option, names, values):
        """
        number : NUMBER
        """
        return float(values[0])

    def on_plusexp(self, target, option, names, values):
        """
        plusexp : exp PLUS exp
        """
        return values[0] + values[2]

    def on_minusexp(self, target, option, names, values):
        """
        minusexp : exp MINUS exp
        """
        return values[0] - values[2]

    def on_timesexp(self, target, option, names, values):
        """
        timesexp : exp TIMES exp
        """
        return values[0] * values[2]

    def on_divexp(self, target, option, names, values):
        """
        divexp : exp DIVIDE exp
        """
        try:
            return values[0] / values[2]
        except:
            return print("Error: Division by zero.")

    def on_modexp(self, target, option, names, values):
        """
        modexp : exp MOD exp
        """
        try:
            return values[0] % values[2]
        except:
            return print("Error: Modulus by zero.")

    def on_powexp(self, target, option, names, values):
        """
        powexp : exp POW exp
        """
        return values[0] ** values[2]

    def on_negexp(self, target, option, names, values):
        """
        negexp : MINUS exp %prec NEG
        """
        return - values[1]

    def on_parenexp(self, target, option, names, values):
        """
        parenexp : LPAREN exp RPAREN
        """
        return values[1]

    def on_varexp(self, target, option, names, values):
        """
        varexp : IDENTIFIER
        """
        if values[0] in self.vars:
            return self.vars[values[0]]
        else:
            print(f"Error: No such variable '{values[0]}'.")

    def on_functioncall(self, target, option, names, values):
        """
        functioncall : IDENTIFIER LPAREN exp RPAREN
        """
        func = getattr(math, values[0], None)
        if not callable(func):
            print("Error: No such function '%s'" % values[0])
        try:
            return func(values[2])
        except Exception as e:
            print(e)

    def on_constant(self, target, option, names, values):
        """
        constant : PI
                 | E
        """
        return getattr(math, values[0])

    def on_myquit(self, target, option, names, values):
        """
        myquit : QUIT
        """
        print("Goodbye!")
        sys.exit(0)

    # -----------------------------------------
    # Display help
    # -----------------------------------------
    def show_help(self):
        print("This PyBison parser implements a basic scientific calculator")
        print(" * scientific notation now works for numbers, eg '2.3e+12'")
        print(" * you can assign values to variables, eg 'x = 23.2'")
        print(" * the constants 'pi' and 'e' are supported")
        print(" * all the python 'math' module functions are available, eg 'sin(pi/6)'")
        print(" * errors, such as division by zero, are now reported")

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
    
    ([0-9]*\.?)([0-9]+)(e[-+]?[0-9]+)? { returntoken(NUMBER); }
    ([0-9]+)(\.?[0-9]*)(e[-+]?[0-9]+)? { returntoken(NUMBER); }
    "("    { returntoken(LPAREN); }
    ")"    { returntoken(RPAREN); }
    "+"    { returntoken(PLUS); }
    "-"    { returntoken(MINUS); }
    "*"    { returntoken(TIMES); }
    "**"   { returntoken(POW); }
    "/"    { returntoken(DIVIDE); }
    "%"    { returntoken(MOD); }
    "quit" { returntoken(QUIT); }
    "="    { returntoken(EQUALS); }
    "e"    { returntoken(E); }
    "pi"   { returntoken(PI); }
    [a-zA-Z_][0-9a-zA-Z_]* { returntoken(IDENTIFIER); }

    [ \t\v\f] {}
    [\n]   { returntoken(NEWLINE); }
    .      { printf("unknown char %c ignored, yytext=0x%lx\n", yytext[0],
                    yytext); /* ignore bad chars */}

    %%
    
    int yywrap(yyscan_t scanner) { return(1); }
    """


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="PyBison CALC1 Example")
    parser.add_argument("-k", "--keepfiles", action="store_true",
                        help="Keep temporary files used in building parse engine lib")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose messages while parser is running")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable garrulous debug messages from parser engine")
    args = parser.parse_args()

    p = Parser(keepfiles=args.keepfiles, verbose=args.verbose)
    print("Scientific calculator example. Type 'help' for help")

    while True:
        try:
            s = input()
            r = p.parse_string(s, debug=args.debug)
            print(r)
        except (KeyboardInterrupt, EOFError):
            break
