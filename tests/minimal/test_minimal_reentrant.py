#!/usr/bin/env python
from bison import BisonParser
import os


class MinimalParser(BisonParser):
    """
    Implements a minimal parser, capable of parsing variable simple definition lists of the following form:
        variablename=42
        othervariable=2
        lastvariable=1
    Grammar rules are defined in the method docstrings. Scanner rules are in the 'lexscript' attribute.
    """

    def run(self, **kwargs):
        self.last_list = []
        return super().run(**kwargs)

    def __init__(self, **kwargs):

        # Declare the start target here (by name)
        # And additional options to the grammar
        self.start = "input"
        self.options = [
            "%define api.pure full",
            "%define api.push-pull push",
            "%lex-param {yyscan_t scanner}",
            "%parse-param {yyscan_t scanner}",
            "%define api.value.type {void *}",
        ]

        # ----------------------------------------------------------------
        # lexer tokens - these must match those in your lex script (below)
        # ----------------------------------------------------------------
        self.tokens = ["STRING", "NUMBER", "NEWLINE", "EQUAL"]

        # ------------------------------
        # precedences
        # ------------------------------
        self.precedences = ()

        # $$
        # -----------------------------------------
        # raw lex script, verbatim here
        # -----------------------------------------

        self.lexscript = r"""
        %option reentrant bison-bridge bison-locations

        %{
        #include "tmp.tab.h"
        #include "Python.h"

        extern void *py_parser;
        extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);

        PyMODINIT_FUNC PyInit_MinimalParser(void) { /* windows needs this function */ }

        #define returntoken(tok)                                       \
                *yylval = (void*)PyUnicode_FromString(strdup(yytext)); \
                return tok;
        #define YY_INPUT(buf,result,max_size) {                        \
            (*py_input)(py_parser, buf, &result, max_size);            \
        }
        %}

        %%

        \n                                      { returntoken(NEWLINE); }
        [a-zA-Z_]+                              { returntoken(STRING); }
        [0-9]+                                  { returntoken(NUMBER); }
        =                                       { returntoken(EQUAL); }

        %%

        int yywrap(yyscan_t scanner) {
          /* we will just terminate when we reach the end of the input file */
          return 1;
        }

        """

        super(MinimalParser, self).__init__(**kwargs)

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    def on_input(self, target, option, names, values):
        """
        input : definition
              | definition NEWLINE input
        """
        append = "" if option == 0 else values[2]
        return f"{target.upper()}({values[0]})\n{append}"

    def on_definition(self, target, option, names, values):
        """
        definition : STRING EQUAL NUMBER
        """
        return ", ".join([f"{n}:{v}" for n, v in zip(names, values)])


def run_minimal_reentrant():
    parser = MinimalParser()
    s = """first=42
second=222222
third=111111111111111111111111111111111111111"""
    snd = parser.parse_string(s)
    print("input:")
    print(s)
    print()
    print("output:")
    print(snd)


def test_minimal_reentrant(capsys):
    run_minimal_reentrant()
    assert (
        capsys.readouterr().out
        == """
input:
first=42
second=222222
third=111111111111111111111111111111111111111

output:
INPUT(STRING:first, EQUAL:=, NUMBER:42)
INPUT(STRING:second, EQUAL:=, NUMBER:222222)
INPUT(STRING:third, EQUAL:=, NUMBER:111111111111111111111111111111111111111)

""".lstrip()
    )


if __name__ == "__main__":
    run_minimal_reentrant()
