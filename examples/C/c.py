#!/usr/bin/env python
"""
PyBison file automatically generated from grammar file c.y
You can edit this module, or import it and subclass the Parser class
"""

from bison import BisonParser, BisonNode

bisonFile = 'c.y'  # original bison file
lexFile = 'c.l'    # original flex file


class ParseNode(BisonNode):
    """
    This is the base class from which all your
    parse nodes are derived.
    Add methods to this class as you need them
    """
    def __init__(self, **kw):
        BisonNode.__init__(self, **kw)

    def __str__(self):
        """Customise as needed"""
        return '<%s instance at 0x%x>' % (self.__class__.__name__, hash(self))

    def __repr__(self):
        """Customise as needed"""
        return str(self)

    def dump(self, indent=0):
        """
        Dump out human-readable, indented parse tree
        Customise as needed - here, or in the node-specific subclasses
        """
        BisonNode.dump(self, indent)   # alter as needed


# ------------------------------------------------------
# Define a node class for each grammar target
# ------------------------------------------------------

class primary_expression_Node(ParseNode):
    """
    Holds a "primary_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class postfix_expression_Node(ParseNode):
    """
    Holds a "postfix_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class argument_expression_list_Node(ParseNode):
    """
    Holds an "argument_expression_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class unary_expression_Node(ParseNode):
    """
    Holds an "unary_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class unary_operator_Node(ParseNode):
    """
    Holds an "unary_operator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class cast_expression_Node(ParseNode):
    """
    Holds a "cast_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class multiplicative_expression_Node(ParseNode):
    """
    Holds a "multiplicative_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class additive_expression_Node(ParseNode):
    """
    Holds an "additive_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class shift_expression_Node(ParseNode):
    """
    Holds a "shift_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class relational_expression_Node(ParseNode):
    """
    Holds a "relational_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class equality_expression_Node(ParseNode):
    """
    Holds an "equality_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class and_expression_Node(ParseNode):
    """
    Holds an "and_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class exclusive_or_expression_Node(ParseNode):
    """
    Holds an "exclusive_or_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class inclusive_or_expression_Node(ParseNode):
    """
    Holds an "inclusive_or_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class logical_and_expression_Node(ParseNode):
    """
    Holds a "logical_and_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class logical_or_expression_Node(ParseNode):
    """
    Holds a "logical_or_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class conditional_expression_Node(ParseNode):
    """
    Holds a "conditional_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class assignment_expression_Node(ParseNode):
    """
    Holds an "assignment_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class assignment_operator_Node(ParseNode):
    """
    Holds an "assignment_operator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class expression_Node(ParseNode):
    """
    Holds an "expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class constant_expression_Node(ParseNode):
    """
    Holds a "constant_expression" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class declaration_Node(ParseNode):
    """
    Holds a "declaration" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class declaration_specifiers_Node(ParseNode):
    """
    Holds a "declaration_specifiers" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class init_declarator_list_Node(ParseNode):
    """
    Holds an "init_declarator_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class init_declarator_Node(ParseNode):
    """
    Holds an "init_declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class storage_class_specifier_Node(ParseNode):
    """
    Holds a "storage_class_specifier" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class type_specifier_Node(ParseNode):
    """
    Holds a "type_specifier" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_or_union_specifier_Node(ParseNode):
    """
    Holds a "struct_or_union_specifier" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_or_union_Node(ParseNode):
    """
    Holds a "struct_or_union" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_declaration_list_Node(ParseNode):
    """
    Holds a "struct_declaration_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_declaration_Node(ParseNode):
    """
    Holds a "struct_declaration" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class specifier_qualifier_list_Node(ParseNode):
    """
    Holds a "specifier_qualifier_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_declarator_list_Node(ParseNode):
    """
    Holds a "struct_declarator_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class struct_declarator_Node(ParseNode):
    """
    Holds a "struct_declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class enum_specifier_Node(ParseNode):
    """
    Holds an "enum_specifier" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class enumerator_list_Node(ParseNode):
    """
    Holds an "enumerator_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class enumerator_Node(ParseNode):
    """
    Holds an "enumerator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class type_qualifier_Node(ParseNode):
    """
    Holds a "type_qualifier" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class declarator_Node(ParseNode):
    """
    Holds a "declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class direct_declarator_Node(ParseNode):
    """
    Holds a "direct_declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class pointer_Node(ParseNode):
    """
    Holds a "pointer" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class type_qualifier_list_Node(ParseNode):
    """
    Holds a "type_qualifier_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class parameter_type_list_Node(ParseNode):
    """
    Holds a "parameter_type_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class parameter_list_Node(ParseNode):
    """
    Holds a "parameter_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class parameter_declaration_Node(ParseNode):
    """
    Holds a "parameter_declaration" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class identifier_list_Node(ParseNode):
    """
    Holds an "identifier_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class type_name_Node(ParseNode):
    """
    Holds a "type_name" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class abstract_declarator_Node(ParseNode):
    """
    Holds an "abstract_declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class direct_abstract_declarator_Node(ParseNode):
    """
    Holds a "direct_abstract_declarator" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class initializer_Node(ParseNode):
    """
    Holds an "initializer" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class initializer_list_Node(ParseNode):
    """
    Holds an "initializer_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class statement_Node(ParseNode):
    """
    Holds a "statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class labeled_statement_Node(ParseNode):
    """
    Holds a "labeled_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class compound_statement_Node(ParseNode):
    """
    Holds a "compound_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class declaration_list_Node(ParseNode):
    """
    Holds a "declaration_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class statement_list_Node(ParseNode):
    """
    Holds a "statement_list" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class expression_statement_Node(ParseNode):
    """
    Holds an "expression_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class selection_statement_Node(ParseNode):
    """
    Holds a "selection_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class iteration_statement_Node(ParseNode):
    """
    Holds an "iteration_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class jump_statement_Node(ParseNode):
    """
    Holds a "jump_statement" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class translation_unit_Node(ParseNode):
    """
    Holds a "translation_unit" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class external_declaration_Node(ParseNode):
    """
    Holds an "external_declaration" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class function_definition_Node(ParseNode):
    """
    Holds a "function_definition" parse target and its components.
    """
    def __init__(self, **kw):
        ParseNode.__init__(self, **kw)

    def dump(self, indent=0):
        ParseNode.dump(self, indent)


class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "c.y" and lex file "c.l"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """

    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = 'c-engine'

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = ['IDENTIFIER', 'CONSTANT', 'STRING_LITERAL', 'SIZEOF', 'PTR_OP', 'INC_OP', 'DEC_OP', 'LEFT_OP', 'RIGHT_OP', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'BOOL_AND_OP', 'BOOL_OR_OP', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'LEFT_ASSIGN', 'RIGHT_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'TYPE_NAME', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'PERIOD', 'COMMA', 'COLON', 'SEMICOLON', 'QUESTIONMARK', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'ASSIGN', 'AND_OP', 'OR_OP', 'BANG', 'TILDE', 'PERCENT', 'CIRCUMFLEX', 'GT_OP', 'LT_OP', 'TYPEDEF', 'EXTERN', 'STATIC', 'AUTO', 'REGISTER', 'CHAR', 'SHORT', 'INT', 'LONG', 'SIGNED', 'UNSIGNED', 'FLOAT', 'DOUBLE', 'CONST', 'VOLATILE', 'VOID', 'STRUCT', 'UNION', 'ENUM', 'ELLIPSIS', 'CASE', 'DEFAULT', 'IF', 'ELSE', 'SWITCH', 'WHILE', 'DO', 'FOR', 'GOTO', 'CONTINUE', 'BREAK', 'RETURN']

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        ('left', ['COMMA'],),
        ('right', ['ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'LEFT_ASSIGN', 'RIGHT_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN'],),
        ('right', ['QUESTIONMARK', 'COLON'],),
        ('left', ['BOOL_OR_OP'],),
        ('left', ['BOOL_AND_OP'],),
        ('left', ['OR_OP'],),
        ('left', ['CIRCUMFLEX'],),
        ('left', ['AND_OP'],),
        ('left', ['EQ_OP', 'NE_OP'],),
        ('left', ['LT_OP', 'GT_OP', 'LE_OP', 'GE_OP'],),
        ('left', ['LEFT_OP', 'RIGHT_OP'],),
        ('left', ['PLUS', 'MINUS'],),
        ('left', ['STAR', 'SLASH', 'PERCENT'],),
        ('right', ['NOT', 'NEG'],),
        ('right', ['INC_OP', 'SIZEOF', 'DEC_OP'],),
        ('left', ['LBRACKET', 'LPAREN', 'PERIOD', 'PTR_OP'],),
        )

    # ---------------------------------------------------------------
    # Declare the start target here (by name)
    # ---------------------------------------------------------------
    start = 'translation_unit'

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    def on_primary_expression(self, target, option, names, values):
        """
        primary_expression
            : IDENTIFIER
            | CONSTANT
            | STRING_LITERAL
            | LPAREN expression RPAREN
        """
        return primary_expression_Node(
            target='primary_expression',
            option=option,
            names=names,
            values=values)

    def on_postfix_expression(self, target, option, names, values):
        """
        postfix_expression
            : primary_expression
            | postfix_expression LBRACKET expression RBRACKET
            | postfix_expression LPAREN RPAREN
            | postfix_expression LPAREN argument_expression_list RPAREN
            | postfix_expression PERIOD IDENTIFIER
            | postfix_expression PTR_OP IDENTIFIER
            | postfix_expression INC_OP
            | postfix_expression DEC_OP
        """
        return postfix_expression_Node(
            target='postfix_expression',
            option=option,
            names=names,
            values=values)

    def on_argument_expression_list(self, target, option, names, values):
        """
        argument_expression_list
            : assignment_expression
            | argument_expression_list COMMA assignment_expression
        """
        return argument_expression_list_Node(
            target='argument_expression_list',
            option=option,
            names=names,
            values=values)

    def on_unary_expression(self, target, option, names, values):
        """
        unary_expression
            : postfix_expression
            | INC_OP unary_expression
            | DEC_OP unary_expression
            | unary_operator cast_expression
            | SIZEOF unary_expression
            | SIZEOF LPAREN type_name RPAREN
        """
        return unary_expression_Node(
            target='unary_expression',
            option=option,
            names=names,
            values=values)

    def on_unary_operator(self, target, option, names, values):
        """
        unary_operator
            : AND_OP
            | STAR
            | PLUS
            | MINUS
            | TILDE
            | BANG
        """
        return unary_operator_Node(
            target='unary_operator',
            option=option,
            names=names,
            values=values)

    def on_cast_expression(self, target, option, names, values):
        """
        cast_expression
            : unary_expression
            | LPAREN type_name RPAREN cast_expression
        """
        return cast_expression_Node(
            target='cast_expression',
            option=option,
            names=names,
            values=values)

    def on_multiplicative_expression(self, target, option, names, values):
        """
        multiplicative_expression
            : cast_expression
            | multiplicative_expression STAR cast_expression
            | multiplicative_expression SLASH cast_expression
            | multiplicative_expression PERCENT cast_expression
        """
        return multiplicative_expression_Node(
            target='multiplicative_expression',
            option=option,
            names=names,
            values=values)

    def on_additive_expression(self, target, option, names, values):
        """
        additive_expression
            : multiplicative_expression
            | additive_expression PLUS multiplicative_expression
            | additive_expression MINUS multiplicative_expression
        """
        return additive_expression_Node(
            target='additive_expression',
            option=option,
            names=names,
            values=values)

    def on_shift_expression(self, target, option, names, values):
        """
        shift_expression
            : additive_expression
            | shift_expression LEFT_OP additive_expression
            | shift_expression RIGHT_OP additive_expression
        """
        return shift_expression_Node(
            target='shift_expression',
            option=option,
            names=names,
            values=values)

    def on_relational_expression(self, target, option, names, values):
        """
        relational_expression
            : shift_expression
            | relational_expression LT_OP shift_expression
            | relational_expression GT_OP shift_expression
            | relational_expression LE_OP shift_expression
            | relational_expression GE_OP shift_expression
        """
        return relational_expression_Node(
            target='relational_expression',
            option=option,
            names=names,
            values=values)

    def on_equality_expression(self, target, option, names, values):
        """
        equality_expression
            : relational_expression
            | equality_expression EQ_OP relational_expression
            | equality_expression NE_OP relational_expression
        """
        return equality_expression_Node(
            target='equality_expression',
            option=option,
            names=names,
            values=values)

    def on_and_expression(self, target, option, names, values):
        """
        and_expression
            : equality_expression
            | and_expression AND_OP equality_expression
        """
        return and_expression_Node(
            target='and_expression',
            option=option,
            names=names,
            values=values)

    def on_exclusive_or_expression(self, target, option, names, values):
        """
        exclusive_or_expression
            : and_expression
            | exclusive_or_expression CIRCUMFLEX and_expression
        """
        return exclusive_or_expression_Node(
            target='exclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_inclusive_or_expression(self, target, option, names, values):
        """
        inclusive_or_expression
            : exclusive_or_expression
            | inclusive_or_expression OR_OP exclusive_or_expression
        """
        return inclusive_or_expression_Node(
            target='inclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_logical_and_expression(self, target, option, names, values):
        """
        logical_and_expression
            : inclusive_or_expression
            | logical_and_expression BOOL_AND_OP inclusive_or_expression
        """
        return logical_and_expression_Node(
            target='logical_and_expression',
            option=option,
            names=names,
            values=values)

    def on_logical_or_expression(self, target, option, names, values):
        """
        logical_or_expression
            : logical_and_expression
            | logical_or_expression BOOL_OR_OP logical_and_expression
        """
        return logical_or_expression_Node(
            target='logical_or_expression',
            option=option,
            names=names,
            values=values)

    def on_conditional_expression(self, target, option, names, values):
        """
        conditional_expression
            : logical_or_expression
            | logical_or_expression QUESTIONMARK expression COLON conditional_expression
        """
        return conditional_expression_Node(
            target='conditional_expression',
            option=option,
            names=names,
            values=values)

    def on_assignment_expression(self, target, option, names, values):
        """
        assignment_expression
            : conditional_expression
            | unary_expression assignment_operator assignment_expression
        """
        return assignment_expression_Node(
            target='assignment_expression',
            option=option,
            names=names,
            values=values)

    def on_assignment_operator(self, target, option, names, values):
        """
        assignment_operator
            : ASSIGN
            | MUL_ASSIGN
            | DIV_ASSIGN
            | MOD_ASSIGN
            | ADD_ASSIGN
            | SUB_ASSIGN
            | LEFT_ASSIGN
            | RIGHT_ASSIGN
            | AND_ASSIGN
            | XOR_ASSIGN
            | OR_ASSIGN
        """
        return assignment_operator_Node(
            target='assignment_operator',
            option=option,
            names=names,
            values=values)

    def on_expression(self, target, option, names, values):
        """
        expression
            : assignment_expression
            | expression COMMA assignment_expression
        """
        return expression_Node(
            target='expression',
            option=option,
            names=names,
            values=values)

    def on_constant_expression(self, target, option, names, values):
        """
        constant_expression
            : conditional_expression
        """
        return constant_expression_Node(
            target='constant_expression',
            option=option,
            names=names,
            values=values)

    def on_declaration(self, target, option, names, values):
        """
        declaration
            : declaration_specifiers SEMICOLON
            | declaration_specifiers init_declarator_list SEMICOLON
        """
        return declaration_Node(
            target='declaration',
            option=option,
            names=names,
            values=values)

    def on_declaration_specifiers(self, target, option, names, values):
        """
        declaration_specifiers
            : storage_class_specifier
            | storage_class_specifier declaration_specifiers
            | type_specifier
            | type_specifier declaration_specifiers
            | type_qualifier
            | type_qualifier declaration_specifiers
        """
        return declaration_specifiers_Node(
            target='declaration_specifiers',
            option=option,
            names=names,
            values=values)

    def on_init_declarator_list(self, target, option, names, values):
        """
        init_declarator_list
            : init_declarator
            | init_declarator_list COMMA init_declarator
        """
        return init_declarator_list_Node(
            target='init_declarator_list',
            option=option,
            names=names,
            values=values)

    def on_init_declarator(self, target, option, names, values):
        """
        init_declarator
            : declarator
            | declarator ASSIGN initializer
        """
        return init_declarator_Node(
            target='init_declarator',
            option=option,
            names=names,
            values=values)

    def on_storage_class_specifier(self, target, option, names, values):
        """
        storage_class_specifier
            : TYPEDEF
            | EXTERN
            | STATIC
            | AUTO
            | REGISTER
        """
        return storage_class_specifier_Node(
            target='storage_class_specifier',
            option=option,
            names=names,
            values=values)

    def on_type_specifier(self, target, option, names, values):
        """
        type_specifier
            : VOID
            | CHAR
            | SHORT
            | INT
            | LONG
            | FLOAT
            | DOUBLE
            | SIGNED
            | UNSIGNED
            | struct_or_union_specifier
            | enum_specifier
            | TYPE_NAME
        """
        return type_specifier_Node(
            target='type_specifier',
            option=option,
            names=names,
            values=values)

    def on_struct_or_union_specifier(self, target, option, names, values):
        """
        struct_or_union_specifier
            : struct_or_union IDENTIFIER LBRACE struct_declaration_list RBRACE
            | struct_or_union LBRACE struct_declaration_list RBRACE
            | struct_or_union IDENTIFIER
        """
        return struct_or_union_specifier_Node(
            target='struct_or_union_specifier',
            option=option,
            names=names,
            values=values)

    def on_struct_or_union(self, target, option, names, values):
        """
        struct_or_union
            : STRUCT
            | UNION
        """
        return struct_or_union_Node(
            target='struct_or_union',
            option=option,
            names=names,
            values=values)

    def on_struct_declaration_list(self, target, option, names, values):
        """
        struct_declaration_list
            : struct_declaration
            | struct_declaration_list struct_declaration
        """
        return struct_declaration_list_Node(
            target='struct_declaration_list',
            option=option,
            names=names,
            values=values)

    def on_struct_declaration(self, target, option, names, values):
        """
        struct_declaration
            : specifier_qualifier_list struct_declarator_list SEMICOLON
        """
        return struct_declaration_Node(
            target='struct_declaration',
            option=option,
            names=names,
            values=values)

    def on_specifier_qualifier_list(self, target, option, names, values):
        """
        specifier_qualifier_list
            : type_specifier specifier_qualifier_list
            | type_specifier
            | type_qualifier specifier_qualifier_list
            | type_qualifier
        """
        return specifier_qualifier_list_Node(
            target='specifier_qualifier_list',
            option=option,
            names=names,
            values=values)

    def on_struct_declarator_list(self, target, option, names, values):
        """
        struct_declarator_list
            : struct_declarator
            | struct_declarator_list COMMA struct_declarator
        """
        return struct_declarator_list_Node(
            target='struct_declarator_list',
            option=option,
            names=names,
            values=values)

    def on_struct_declarator(self, target, option, names, values):
        """
        struct_declarator
            : declarator
            | COLON constant_expression
            | declarator COLON constant_expression
        """
        return struct_declarator_Node(
            target='struct_declarator',
            option=option,
            names=names,
            values=values)

    def on_enum_specifier(self, target, option, names, values):
        """
        enum_specifier
            : ENUM LBRACE enumerator_list RBRACE
            | ENUM IDENTIFIER LBRACE enumerator_list RBRACE
            | ENUM IDENTIFIER
        """
        return enum_specifier_Node(
            target='enum_specifier',
            option=option,
            names=names,
            values=values)

    def on_enumerator_list(self, target, option, names, values):
        """
        enumerator_list
            : enumerator
            | enumerator_list COMMA enumerator
        """
        return enumerator_list_Node(
            target='enumerator_list',
            option=option,
            names=names,
            values=values)

    def on_enumerator(self, target, option, names, values):
        """
        enumerator
            : IDENTIFIER
            | IDENTIFIER ASSIGN constant_expression
        """
        return enumerator_Node(
            target='enumerator',
            option=option,
            names=names,
            values=values)

    def on_type_qualifier(self, target, option, names, values):
        """
        type_qualifier
            : CONST
            | VOLATILE
        """
        return type_qualifier_Node(
            target='type_qualifier',
            option=option,
            names=names,
            values=values)

    def on_declarator(self, target, option, names, values):
        """
        declarator
            : pointer direct_declarator
            | direct_declarator
        """
        return declarator_Node(
            target='declarator',
            option=option,
            names=names,
            values=values)

    def on_direct_declarator(self, target, option, names, values):
        """
        direct_declarator
            : IDENTIFIER
            | LPAREN declarator RPAREN
            | direct_declarator LBRACKET constant_expression RBRACKET
            | direct_declarator LBRACKET RBRACKET
            | direct_declarator LPAREN parameter_type_list RPAREN
            | direct_declarator LPAREN identifier_list RPAREN
            | direct_declarator LPAREN RPAREN
        """
        return direct_declarator_Node(
            target='direct_declarator',
            option=option,
            names=names,
            values=values)

    def on_pointer(self, target, option, names, values):
        """
        pointer
            : STAR
            | STAR type_qualifier_list
            | STAR pointer
            | STAR type_qualifier_list pointer
        """
        return pointer_Node(
            target='pointer',
            option=option,
            names=names,
            values=values)

    def on_type_qualifier_list(self, target, option, names, values):
        """
        type_qualifier_list
            : type_qualifier
            | type_qualifier_list type_qualifier
        """
        return type_qualifier_list_Node(
            target='type_qualifier_list',
            option=option,
            names=names,
            values=values)

    def on_parameter_type_list(self, target, option, names, values):
        """
        parameter_type_list
            : parameter_list
            | parameter_list COMMA ELLIPSIS
        """
        return parameter_type_list_Node(
            target='parameter_type_list',
            option=option,
            names=names,
            values=values)

    def on_parameter_list(self, target, option, names, values):
        """
        parameter_list
            : parameter_declaration
            | parameter_list COMMA parameter_declaration
        """
        return parameter_list_Node(
            target='parameter_list',
            option=option,
            names=names,
            values=values)

    def on_parameter_declaration(self, target, option, names, values):
        """
        parameter_declaration
            : declaration_specifiers declarator
            | declaration_specifiers abstract_declarator
            | declaration_specifiers
        """
        return parameter_declaration_Node(
            target='parameter_declaration',
            option=option,
            names=names,
            values=values)

    def on_identifier_list(self, target, option, names, values):
        """
        identifier_list
            : IDENTIFIER
            | identifier_list COMMA IDENTIFIER
        """
        return identifier_list_Node(
            target='identifier_list',
            option=option,
            names=names,
            values=values)

    def on_type_name(self, target, option, names, values):
        """
        type_name
            : specifier_qualifier_list
            | specifier_qualifier_list abstract_declarator
        """
        return type_name_Node(
            target='type_name',
            option=option,
            names=names,
            values=values)

    def on_abstract_declarator(self, target, option, names, values):
        """
        abstract_declarator
            : pointer
            | direct_abstract_declarator
            | pointer direct_abstract_declarator
        """
        return abstract_declarator_Node(
            target='abstract_declarator',
            option=option,
            names=names,
            values=values)

    def on_direct_abstract_declarator(self, target, option, names, values):
        """
        direct_abstract_declarator
            : LPAREN abstract_declarator RPAREN
            | LBRACKET RBRACKET
            | LBRACKET constant_expression RBRACKET
            | direct_abstract_declarator LBRACKET RBRACKET
            | direct_abstract_declarator LBRACKET constant_expression RBRACKET
            | LPAREN RPAREN
            | LPAREN parameter_type_list RPAREN
            | direct_abstract_declarator LPAREN RPAREN
            | direct_abstract_declarator LPAREN parameter_type_list RPAREN
        """
        return direct_abstract_declarator_Node(
            target='direct_abstract_declarator',
            option=option,
            names=names,
            values=values)

    def on_initializer(self, target, option, names, values):
        """
        initializer
            : assignment_expression
            | LBRACE initializer_list RBRACE
            | LBRACE initializer_list COMMA RBRACE
        """
        return initializer_Node(
            target='initializer',
            option=option,
            names=names,
            values=values)

    def on_initializer_list(self, target, option, names, values):
        """
        initializer_list
            : initializer
            | initializer_list COMMA initializer
        """
        return initializer_list_Node(
            target='initializer_list',
            option=option,
            names=names,
            values=values)

    def on_statement(self, target, option, names, values):
        """
        statement
            : labeled_statement
            | compound_statement
            | expression_statement
            | selection_statement
            | iteration_statement
            | jump_statement
        """
        return statement_Node(
            target='statement',
            option=option,
            names=names,
            values=values)

    def on_labeled_statement(self, target, option, names, values):
        """
        labeled_statement
            : IDENTIFIER COLON statement
            | CASE constant_expression COLON statement
            | DEFAULT COLON statement
        """
        return labeled_statement_Node(
            target='labeled_statement',
            option=option,
            names=names,
            values=values)

    def on_compound_statement(self, target, option, names, values):
        """
        compound_statement
            : LBRACE RBRACE
            | LBRACE statement_list RBRACE
            | LBRACE declaration_list RBRACE
            | LBRACE declaration_list statement_list RBRACE
        """
        return compound_statement_Node(
            target='compound_statement',
            option=option,
            names=names,
            values=values)

    def on_declaration_list(self, target, option, names, values):
        """
        declaration_list
            : declaration
            | declaration_list declaration
        """
        return declaration_list_Node(
            target='declaration_list',
            option=option,
            names=names,
            values=values)

    def on_statement_list(self, target, option, names, values):
        """
        statement_list
            : statement
            | statement_list statement
        """
        return statement_list_Node(
            target='statement_list',
            option=option,
            names=names,
            values=values)

    def on_expression_statement(self, target, option, names, values):
        """
        expression_statement
            : SEMICOLON
            | expression SEMICOLON
        """
        return expression_statement_Node(
            target='expression_statement',
            option=option,
            names=names,
            values=values)

    def on_selection_statement(self, target, option, names, values):
        """
        selection_statement
            : IF LPAREN expression RPAREN statement
            | IF LPAREN expression RPAREN statement ELSE statement
            | SWITCH LPAREN expression RPAREN statement
        """
        return selection_statement_Node(
            target='selection_statement',
            option=option,
            names=names,
            values=values)

    def on_iteration_statement(self, target, option, names, values):
        """
        iteration_statement
            : WHILE LPAREN expression RPAREN statement
            | DO statement WHILE LPAREN expression RPAREN SEMICOLON
            | FOR LPAREN expression_statement expression_statement RPAREN statement
            | FOR LPAREN expression_statement expression_statement expression RPAREN statement
        """
        return iteration_statement_Node(
            target='iteration_statement',
            option=option,
            names=names,
            values=values)

    def on_jump_statement(self, target, option, names, values):
        """
        jump_statement
            : GOTO IDENTIFIER SEMICOLON
            | CONTINUE SEMICOLON
            | BREAK SEMICOLON
            | RETURN SEMICOLON
            | RETURN expression SEMICOLON
        """
        return jump_statement_Node(
            target='jump_statement',
            option=option,
            names=names,
            values=values)

    def on_translation_unit(self, target, option, names, values):
        """
        translation_unit
            : external_declaration
            | translation_unit external_declaration
        """
        return translation_unit_Node(
            target='translation_unit',
            option=option,
            names=names,
            values=values)

    def on_external_declaration(self, target, option, names, values):
        """
        external_declaration
            : function_definition
            | declaration
        """
        return external_declaration_Node(
            target='external_declaration',
            option=option,
            names=names,
            values=values)

    def on_function_definition(self, target, option, names, values):
        """
        function_definition
            : declaration_specifiers declarator declaration_list compound_statement
            | declaration_specifiers declarator compound_statement
            | declarator declaration_list compound_statement
            | declarator compound_statement
        """
        return function_definition_Node(
            target='function_definition',
            option=option,
            names=names,
            values=values)

    # -----------------------------------------
    # raw lex script, verbatim here
    # -----------------------------------------
    lexscript = r"""
D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*


%{

/* this scanner sourced from: http://www.lysator.liu.se/c/ANSI-C-grammar-l.html */

void count();
//int yylineno = 0;
#include <stdio.h>
#include <string.h>
#include "Python.h"
#define YYSTYPE void *
#include "tmp.tab.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) /*printf("%d=%s\n", tok, yytext);*/ yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) { (*py_input)(py_parser, buf, &result, max_size); }

%}


%%
"/*"			{ comment(); }

"auto"			{ count(); returntoken(AUTO); }
"break"			{ count(); returntoken(BREAK); }
"case"			{ count(); returntoken(CASE); }
"char"			{ count(); returntoken(CHAR); }
"const"			{ count(); returntoken(CONST); }
"continue"		{ count(); returntoken(CONTINUE); }
"default"		{ count(); returntoken(DEFAULT); }
"do"			{ count(); returntoken(DO); }
"double"		{ count(); returntoken(DOUBLE); }
"else"			{ count(); returntoken(ELSE); }
"enum"			{ count(); returntoken(ENUM); }
"extern"		{ count(); returntoken(EXTERN); }
"float"			{ count(); returntoken(FLOAT); }
"for"			{ count(); returntoken(FOR); }
"goto"			{ count(); returntoken(GOTO); }
"if"			{ count(); returntoken(IF); }
"int"			{ count(); returntoken(INT); }
"long"			{ count(); returntoken(LONG); }
"register"		{ count(); returntoken(REGISTER); }
"return"		{ count(); returntoken(RETURN); }
"short"			{ count(); returntoken(SHORT); }
"signed"		{ count(); returntoken(SIGNED); }
"sizeof"		{ count(); returntoken(SIZEOF); }
"static"		{ count(); returntoken(STATIC); }
"struct"		{ count(); returntoken(STRUCT); }
"switch"		{ count(); returntoken(SWITCH); }
"typedef"		{ count(); returntoken(TYPEDEF); }
"union"			{ count(); returntoken(UNION); }
"unsigned"		{ count(); returntoken(UNSIGNED); }
"void"			{ count(); returntoken(VOID); }
"volatile"		{ count(); returntoken(VOLATILE); }
"while"			{ count(); returntoken(WHILE); }

{L}({L}|{D})*		{ count(); returntoken(check_type()); }

0[xX]{H}+{IS}?		{ count(); returntoken(CONSTANT); }
0{D}+{IS}?		{ count(); returntoken(CONSTANT); }
{D}+{IS}?		{ count(); returntoken(CONSTANT); }
L?'(\\.|[^\\'])+'	{ count(); returntoken(CONSTANT); }

{D}+{E}{FS}?		{ count(); returntoken(CONSTANT); }
{D}*"."{D}+({E})?{FS}?	{ count(); returntoken(CONSTANT); }
{D}+"."{D}*({E})?{FS}?	{ count(); returntoken(CONSTANT); }

L?\"(\\.|[^\\"])*\"	{ count(); returntoken(STRING_LITERAL); }

"..."			{ count(); returntoken(ELLIPSIS); }
">>="			{ count(); returntoken(RIGHT_ASSIGN); }
"<<="			{ count(); returntoken(LEFT_ASSIGN); }
"+="			{ count(); returntoken(ADD_ASSIGN); }
"-="			{ count(); returntoken(SUB_ASSIGN); }
"*="			{ count(); returntoken(MUL_ASSIGN); }
"/="			{ count(); returntoken(DIV_ASSIGN); }
"%="			{ count(); returntoken(MOD_ASSIGN); }
"&="			{ count(); returntoken(AND_ASSIGN); }
"^="			{ count(); returntoken(XOR_ASSIGN); }
"|="			{ count(); returntoken(OR_ASSIGN); }
">>"			{ count(); returntoken(RIGHT_OP); }
"<<"			{ count(); returntoken(LEFT_OP); }
"++"			{ count(); returntoken(INC_OP); }
"--"			{ count(); returntoken(DEC_OP); }
"->"			{ count(); returntoken(PTR_OP); }
"&&"			{ count(); returntoken(BOOL_AND_OP); }
"||"			{ count(); returntoken(BOOL_OR_OP); }
"<="			{ count(); returntoken(LE_OP); }
">="			{ count(); returntoken(GE_OP); }
"=="			{ count(); returntoken(EQ_OP); }
"!="			{ count(); returntoken(NE_OP); }
";"			{ count(); returntoken(SEMICOLON); }
("{"|"<%")		{ count(); returntoken(LBRACE); }
("}"|"%>")		{ count(); returntoken(RBRACE); }
","			{ count(); returntoken(COMMA); }
":"			{ count(); returntoken(COLON); }
"="			{ count(); returntoken(ASSIGN); }
"("			{ count(); returntoken(LPAREN); }
")"			{ count(); returntoken(RPAREN); }
("["|"<:")		{ count(); returntoken(LBRACKET); }
("]"|":>")		{ count(); returntoken(RBRACKET); }
"."			{ count(); returntoken(PERIOD); }
"&"			{ count(); returntoken(AND_OP); }
"!"			{ count(); returntoken(BANG); }
"~"			{ count(); returntoken(TILDE); }
"-"			{ count(); returntoken(MINUS); }
"+"			{ count(); returntoken(PLUS); }
"*"			{ count(); returntoken(STAR); }
"/"			{ count(); returntoken(SLASH); }
"%"			{ count(); returntoken(PERCENT); }
"<"			{ count(); returntoken(LT_OP); }
">"			{ count(); returntoken(GT_OP); }
"^"			{ count(); returntoken(CIRCUMFLEX); }
"|"			{ count(); returntoken(OR_OP); }
"?"			{ count(); returntoken(QUESTIONMARK); }

[ \t\v\n\f]		{ count(); }
.			{ /* ignore bad characters */ }

%%

yywrap()
{
    return(1);
}


comment()
{
    char c, c1;

loop:
    while ((c = input()) != '*' && c != 0)
        /*putchar(c)*/;

    if ((c1 = input()) != '/' && c != 0)
    {
        unput(c1);
        goto loop;
    }

    if (c != 0)
        /*putchar(c1)*/;
}


int column = 0;

void count()
{
    int i;

    for (i = 0; yytext[i] != '\0'; i++)
        if (yytext[i] == '\n')
            column = 0;
        else if (yytext[i] == '\t')
            column += 8 - (column % 8);
        else
            column++;

    /*ECHO*/;
}


int check_type()
{
/*
* pseudo code --- this is what it should check
*
*	if (yytext == type_name)
*		return(TYPE_NAME);
*
*	return(IDENTIFIER);
*/

/*
*	it actually will only return IDENTIFIER
*/

    return(IDENTIFIER);
}

"""
# -----------------------------------------
# end raw lex script
# -----------------------------------------


def main():
    """
    Unit-testing func
    """
    import argparse
    parser = argparse.ArgumentParser(prog="PyBison C Example")
    parser.add_argument("-k", "--keepfiles", action="store_true",
                        help="Keep temporary files used in building parse engine lib")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose messages while parser is running")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable garrulous debug messages from parser engine")
    parser.add_argument("filename", type=str, nargs="*",
                        help="path of a file to parse, defaults to stdin")
    args = parser.parse_args()

    if isinstance(args.filename, list) and len(args.filename) == 0:
        args.filename = None

    p = Parser(verbose=args.verbose, keepfiles=args.keepfiles)
    forrest = []
    if args.filename is None:
        print("(Reading from standard input - please type stuff)")
        tree = p.run(file=None, debug=args.debug)
        forrest.append(tree)
    else:
        for fp in args.filename:
            tree = p.run(file=fp, debug=args.debug)
            forrest.append(tree)
    return forrest


if __name__ == '__main__':
    main()
