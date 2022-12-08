#!/usr/bin/env python
from bison import BisonParser


class JSONParser(BisonParser):
    """Implements a JSON parser.
    Grammar rules are defined in the method docstrings.
    Scanner rules are in the 'lexscript' attribute.
    """

    def run(self, **kwargs):
        self.last_list = []
        return super().run(**kwargs)

    def __init__(self, **kwargs):

        # Declare the start target here (by name)
        # And additional options to the grammar
        self.start = "value"
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
        self.tokens = ["INTEGER", "FLOAT", "BOOL", "STRING",
                       "O_START", "O_END", "A_START", "A_END",
                       "COMMA", "COLON", "_"]

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

        PyMODINIT_FUNC PyInit_JSONParser(void) { /* windows needs this function */ }

        #define returntoken(tok)                                       \
                *yylval = (void*)PyUnicode_FromString(strdup(yytext)); \
                return tok;
        #define YY_INPUT(buf,result,max_size) {                        \
            (*py_input)(py_parser, buf, &result, max_size);            \
        }
        %}

        %%


        -?[0-9]+                                { returntoken(INTEGER); } 
        -?[0-9]+([.][0-9]+)?([eE]-?[0-9]+)?     { returntoken(FLOAT); } 
        false|true|null                         { returntoken(BOOL); } 
        \"([^\"]|\\[.])*\"                      { returntoken(STRING); } 
        \{                                      { returntoken(O_START); } 
        \}                                      { returntoken(O_END); } 
        \[                                      { returntoken(A_START); } 
        \]                                      { returntoken(A_END); } 
        ,                                       { returntoken(COMMA); } 
        :                                       { returntoken(COLON); } 
        [ \t\n]                                 {  }


        %%

        int yywrap(yyscan_t scanner) {
          /* we will just terminate when we reach the end of the input file */
          return 1;
        }

        """
        super(JSONParser, self).__init__(**kwargs)

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

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


def test_compile_json_reentrant():
    JSONParser()


def test_json_parser():
    import json
    import pathlib

    parser = JSONParser()

    file = pathlib.Path(__file__).parent.resolve() / "example.json"
    result_bison = parser.run(file=str(file))

    with open(file) as fh:
        result_json = json.load(fh)

    assert result_bison == result_json


if __name__ == '__main__':
    test_json_parser()
