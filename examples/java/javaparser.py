#!/usr/bin/env python

"""
PyBison file automatically generated from grammar file javaparser.y
You can edit this module, or import it and subclass the Parser class
"""


from bison import BisonParser, BisonNode

bisonFile = 'javaparser.y'  # original bison file
lexFile = 'javaparser.l'    # original flex file


class Parser(BisonParser):
    """
    bison Parser class generated automatically by bison2py from the
    grammar file "javaparser.y" and lex file "javaparser.l"

    You may (and probably should) edit the methods in this class.
    You can freely edit the rules (in the method docstrings), the
    tokens list, the start symbol, and the precedences.

    Each time this class is instantiated, a hashing technique in the
    base class detects if you have altered any of the rules. If any
    changes are detected, a new dynamic lib for the parser engine
    will be generated automatically.
    """
    options = ["%define api.value.type {void *}"]

    # -------------------------------------------------
    # Default class to use for creating new parse nodes
    # -------------------------------------------------
    defaultNodeClass = BisonNode

    # --------------------------------------------
    # basename of binary parser engine dynamic lib
    # --------------------------------------------
    bisonEngineLibName = 'javaparser-engine'

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = ['PLUS_TOKEN', 'MINUS_TOKEN', 'MUL_TOKEN', 'DIV_TOKEN', 'MOD_TOKEN', 'SHL_TOKEN', 'SHR_TOKEN', 'SAR_TOKEN', 'AND_TOKEN', 'XOR_TOKEN', 'OR_TOKEN', 'LOGICAL_AND_TOKEN', 'LOGICAL_OR_TOKEN', 'EQ_TOKEN', 'NE_OP_TOKEN', 'GREATER_TOKEN', 'GE_TOKEN', 'LESS_TOKEN', 'LE_TOKEN', 'ADD_ASSIGN_TOKEN', 'SUB_ASSIGN_TOKEN', 'MUL_ASSIGN_TOKEN', 'DIV_ASSIGN_TOKEN', 'MOD_ASSIGN_TOKEN', 'SHL_ASSIGN_TOKEN', 'SHR_ASSIGN_TOKEN', 'SAR_ASSIGN_TOKEN', 'AND_ASSIGN_TOKEN', 'XOR_ASSIGN_TOKEN', 'OR_ASSIGN_TOKEN', 'PUBLIC_TOKEN', 'PRIVATE_TOKEN', 'PROTECTED_TOKEN', 'STATIC_TOKEN', 'FINAL_TOKEN', 'SYNCHRONIZED_TOKEN', 'VOLATILE_TOKEN', 'TRANSIENT_TOKEN', 'NATIVE_TOKEN', 'PAD_TOKEN', 'ABSTRACT_TOKEN', 'MODIFIER_TOKEN', 'STRICT_TOKEN', 'STRICTFP_TOKEN', 'DEC_TOKEN', 'INC_TOKEN', 'DEFAULT_TOKEN', 'IF_TOKEN', 'THROW_TOKEN', 'BOOLEAN_TOKEN', 'DO_TOKEN', 'IMPLEMENTS_TOKEN', 'THROWS_TOKEN', 'BREAK_TOKEN', 'IMPORT_TOKEN', 'ELSE_TOKEN', 'INSTANCEOF_TOKEN', 'RETURN_TOKEN', 'VOID_TOKEN', 'CATCH_TOKEN', 'INTERFACE_TOKEN', 'CASE_TOKEN', 'EXTENDS_TOKEN', 'FINALLY_TOKEN', 'SUPER_TOKEN', 'WHILE_TOKEN', 'CLASS_TOKEN', 'SWITCH_TOKEN', 'CONST_TOKEN', 'TRY_TOKEN', 'FOR_TOKEN', 'NEW_TOKEN', 'CONTINUE_TOKEN', 'GOTO_TOKEN', 'PACKAGE_TOKEN', 'THIS_TOKEN', 'ASSERT_TOKEN', 'BYTE_TOKEN', 'SHORT_TOKEN', 'INT_TOKEN', 'LONG_TOKEN', 'CHAR_TOKEN', 'FLOAT_TOKEN', 'DOUBLE_TOKEN', 'ID_TOKEN', 'CONDITIONAL_TOKEN', 'COLON_TOKEN', 'TILDE_TOKEN', 'NOT_TOKEN', 'ASSIGN_ANY_TOKEN', 'ASSIGNS_TOKEN', 'OPEN_PAREN_TOKEN', 'CLOSE_PAREN_TOKEN', 'OPEN_BRACE_TOKEN', 'CLOSE_BRACE_TOKEN', 'OPEN_BRACKET_TOKEN', 'CLOSE_BRACKET_TOKEN', 'SEMICOLON_TOKEN', 'COMMA_TOKEN', 'PERIOD_TOKEN', 'INTEGER_LITERAL_TOKEN', 'FLOATING_POINT_LITERAL_TOKEN', 'BOOLEAN_LITERAL_TOKEN', 'STRING_LITERAL_TOKEN', 'CHARACTER_LITERAL_TOKEN', 'NULL_TOKEN']

    # ------------------------------
    # precedences
    # ------------------------------
    precedences = (
        ('right', ['SHL_ASSIGN_TOKEN', 'SAR_ASSIGN_TOKEN', 'AND_ASSIGN_TOKEN', 'OR_ASSIGN_TOKEN', 'XOR_ASSIGN_TOKEN', 'ASSIGNS_TOKEN', 'ADD_ASSIGN_TOKEN', 'SUB_ASSIGN_TOKEN', 'MUL_ASSIGN_TOKEN', 'DIV_ASSIGN_TOKEN', 'MOD_ASSIGN_TOKEN'],),
        ('left', ['LOGICAL_OR_TOKEN'],),
        ('left', ['LOGICAL_AND_TOKEN'],),
        ('left', ['OR_TOKEN'],),
        ('left', ['XOR_TOKEN'],),
        ('left', ['AND_TOKEN'],),
        ('left', ['RELATIVEQEUAL_TOKEN', 'NE_OP_TOKEN'],),
        ('left', ['GREATER_TOKEN', 'LESS_TOKEN', 'GE_TOKEN', 'LE_TOKEN'],),
        ('left', ['SHL_TOKEN', 'SAR_TOKEN', 'SHR_TOKEN'],),
        ('left', ['PLUS_TOKEN', 'MINUS_TOKEN'],),
        ('left', ['MUL_TOKEN', 'DIV_TOKEN', 'MOD_TOKEN'],),
        ('nonassoc', ['NOT_TOKEN', 'TILDE_TOKEN'],),
        )

    # ---------------------------------------------------------------
    # Declare the start target here (by name)
    # ---------------------------------------------------------------
    start = 'goal'

    # ---------------------------------------------------------------
    # These methods are the python handlers for the bison targets.
    # (which get called by the bison code each time the corresponding
    # parse target is unambiguously reached)
    #
    # WARNING - don't touch the method docstrings unless you know what
    # you are doing - they are in bison rule syntax, and are passed
    # verbatim to bison to build the parser engine library.
    # ---------------------------------------------------------------

    def on_goal(self, target, option, names, values):
        """
        goal
            : compilation_unit
        """
        return self.defaultNodeClass(
            target='goal',
            option=option,
            names=names,
            values=values)

    def on_literal(self, target, option, names, values):
        """
        literal
            : INTEGER_LITERAL_TOKEN
            | FLOATING_POINT_LITERAL_TOKEN
            | BOOLEAN_LITERAL_TOKEN
            | CHARACTER_LITERAL_TOKEN
            | STRING_LITERAL_TOKEN
            | NULL_TOKEN
        """
        return self.defaultNodeClass(
            target='literal',
            option=option,
            names=names,
            values=values)

    def on_type(self, target, option, names, values):
        """
        type
            : primitive_type
            | reference_type
        """
        return self.defaultNodeClass(
            target='type',
            option=option,
            names=names,
            values=values)

    def on_primitive_type(self, target, option, names, values):
        """
        primitive_type
            : INT_TOKEN
            | LONG_TOKEN
            | FLOAT_TOKEN
            | DOUBLE_TOKEN
            | BOOLEAN_TOKEN
            | BYTE_TOKEN
            | CHAR_TOKEN
            | SHORT_TOKEN
        """
        return self.defaultNodeClass(
            target='primitive_type',
            option=option,
            names=names,
            values=values)

    def on_reference_type(self, target, option, names, values):
        """
        reference_type
            : class_or_interface_type
            | array_type
        """
        return self.defaultNodeClass(
            target='reference_type',
            option=option,
            names=names,
            values=values)

    def on_class_or_interface_type(self, target, option, names, values):
        """
        class_or_interface_type
            : name
        """
        return self.defaultNodeClass(
            target='class_or_interface_type',
            option=option,
            names=names,
            values=values)

    def on_class_type(self, target, option, names, values):
        """
        class_type
            : class_or_interface_type
        """
        return self.defaultNodeClass(
            target='class_type',
            option=option,
            names=names,
            values=values)

    def on_interface_type(self, target, option, names, values):
        """
        interface_type
            : class_or_interface_type
        """
        return self.defaultNodeClass(
            target='interface_type',
            option=option,
            names=names,
            values=values)

    def on_array_type(self, target, option, names, values):
        """
        array_type
            : primitive_type dims
            | name dims
        """
        return self.defaultNodeClass(
            target='array_type',
            option=option,
            names=names,
            values=values)

    def on_name(self, target, option, names, values):
        """
        name
            : simple_name
            | qualified_name
        """
        return self.defaultNodeClass(
            target='name',
            option=option,
            names=names,
            values=values)

    def on_simple_name(self, target, option, names, values):
        """
        simple_name
            : identifier
        """
        return self.defaultNodeClass(
            target='simple_name',
            option=option,
            names=names,
            values=values)

    def on_qualified_name(self, target, option, names, values):
        """
        qualified_name
            : name PERIOD_TOKEN identifier
        """
        return self.defaultNodeClass(
            target='qualified_name',
            option=option,
            names=names,
            values=values)

    def on_identifier(self, target, option, names, values):
        """
        identifier
            : ID_TOKEN
        """
        return self.defaultNodeClass(
            target='identifier',
            option=option,
            names=names,
            values=values)

    def on_compilation_unit(self, target, option, names, values):
        """
        compilation_unit
            : | package_declaration
            | import_declarations
            | type_declarations
            | package_declaration import_declarations
            | package_declaration type_declarations
            | import_declarations type_declarations
            | package_declaration import_declarations type_declarations
        """
        return self.defaultNodeClass(
            target='compilation_unit',
            option=option,
            names=names,
            values=values)

    def on_import_declarations(self, target, option, names, values):
        """
        import_declarations
            : import_declaration
            | import_declarations import_declaration
        """
        return self.defaultNodeClass(
            target='import_declarations',
            option=option,
            names=names,
            values=values)

    def on_type_declarations(self, target, option, names, values):
        """
        type_declarations
            : type_declaration
            | type_declarations type_declaration
        """
        return self.defaultNodeClass(
            target='type_declarations',
            option=option,
            names=names,
            values=values)

    def on_package_declaration(self, target, option, names, values):
        """
        package_declaration
            : PACKAGE_TOKEN name SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='package_declaration',
            option=option,
            names=names,
            values=values)

    def on_import_declaration(self, target, option, names, values):
        """
        import_declaration
            : single_type_import_declaration
            | type_import_on_demand_declaration
        """
        return self.defaultNodeClass(
            target='import_declaration',
            option=option,
            names=names,
            values=values)

    def on_single_type_import_declaration(self, target, option, names, values):
        """
        single_type_import_declaration
            : IMPORT_TOKEN name SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='single_type_import_declaration',
            option=option,
            names=names,
            values=values)

    def on_type_import_on_demand_declaration(self, target, option, names, values):
        """
        type_import_on_demand_declaration
            : IMPORT_TOKEN name PERIOD_TOKEN MUL_TOKEN SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='type_import_on_demand_declaration',
            option=option,
            names=names,
            values=values)

    def on_type_declaration(self, target, option, names, values):
        """
        type_declaration
            : class_declaration
            | interface_declaration
            | empty_statement
        """
        return self.defaultNodeClass(
            target='type_declaration',
            option=option,
            names=names,
            values=values)

    def on_modifiers(self, target, option, names, values):
        """
        modifiers
            : modifier
            | modifiers modifier
        """
        return self.defaultNodeClass(
            target='modifiers',
            option=option,
            names=names,
            values=values)

    def on_modifier(self, target, option, names, values):
        """
        modifier
            : STATIC_TOKEN
            | PUBLIC_TOKEN
            | PROTECTED_TOKEN
            | PRIVATE_TOKEN
            | ABSTRACT_TOKEN
            | FINAL_TOKEN
            | NATIVE_TOKEN
            | SYNCHRONIZED_TOKEN
            | TRANSIENT_TOKEN
            | VOLATILE_TOKEN
        """
        return self.defaultNodeClass(
            target='modifier',
            option=option,
            names=names,
            values=values)

    def on_class_declaration(self, target, option, names, values):
        """
        class_declaration
            : modifiers CLASS_TOKEN identifier super interfaces class_body
            | CLASS_TOKEN identifier super interfaces class_body
        """
        return self.defaultNodeClass(
            target='class_declaration',
            option=option,
            names=names,
            values=values)

    def on_super(self, target, option, names, values):
        """
        super
            : | EXTENDS_TOKEN class_type
        """
        return self.defaultNodeClass(
            target='super',
            option=option,
            names=names,
            values=values)

    def on_interfaces(self, target, option, names, values):
        """
        interfaces
            : | IMPLEMENTS_TOKEN interface_type_list
        """
        return self.defaultNodeClass(
            target='interfaces',
            option=option,
            names=names,
            values=values)

    def on_interface_type_list(self, target, option, names, values):
        """
        interface_type_list
            : interface_type
            | interface_type_list COMMA_TOKEN interface_type
        """
        return self.defaultNodeClass(
            target='interface_type_list',
            option=option,
            names=names,
            values=values)

    def on_class_body(self, target, option, names, values):
        """
        class_body
            : OPEN_BRACE_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN class_body_declarations CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='class_body',
            option=option,
            names=names,
            values=values)

    def on_class_body_declarations(self, target, option, names, values):
        """
        class_body_declarations
            : class_body_declaration
            | class_body_declarations class_body_declaration
        """
        return self.defaultNodeClass(
            target='class_body_declarations',
            option=option,
            names=names,
            values=values)

    def on_class_body_declaration(self, target, option, names, values):
        """
        class_body_declaration
            : class_member_declaration
            | static_initializer
            | constructor_declaration
            | block
        """
        return self.defaultNodeClass(
            target='class_body_declaration',
            option=option,
            names=names,
            values=values)

    def on_class_member_declaration(self, target, option, names, values):
        """
        class_member_declaration
            : field_declaration
            | method_declaration
            | class_declaration
            | interface_declaration
            | empty_statement
        """
        return self.defaultNodeClass(
            target='class_member_declaration',
            option=option,
            names=names,
            values=values)

    def on_field_declaration(self, target, option, names, values):
        """
        field_declaration
            : type variable_declarators SEMICOLON_TOKEN
            | modifiers type variable_declarators SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='field_declaration',
            option=option,
            names=names,
            values=values)

    def on_variable_declarators(self, target, option, names, values):
        """
        variable_declarators
            : variable_declarator
            | variable_declarators COMMA_TOKEN variable_declarator
        """
        return self.defaultNodeClass(
            target='variable_declarators',
            option=option,
            names=names,
            values=values)

    def on_variable_declarator(self, target, option, names, values):
        """
        variable_declarator
            : variable_declarator_id
            | variable_declarator_id ASSIGNS_TOKEN variable_initializer
        """
        return self.defaultNodeClass(
            target='variable_declarator',
            option=option,
            names=names,
            values=values)

    def on_variable_declarator_id(self, target, option, names, values):
        """
        variable_declarator_id
            : identifier
            | variable_declarator_id OPEN_BRACKET_TOKEN CLOSE_BRACKET_TOKEN
        """
        return self.defaultNodeClass(
            target='variable_declarator_id',
            option=option,
            names=names,
            values=values)

    def on_variable_initializer(self, target, option, names, values):
        """
        variable_initializer
            : expression
            | array_initializer
        """
        return self.defaultNodeClass(
            target='variable_initializer',
            option=option,
            names=names,
            values=values)

    def on_method_declaration(self, target, option, names, values):
        """
        method_declaration
            : method_header method_body
        """
        return self.defaultNodeClass(
            target='method_declaration',
            option=option,
            names=names,
            values=values)

    def on_method_header(self, target, option, names, values):
        """
        method_header
            : type method_declarator throws
            | VOID_TOKEN method_declarator throws
            | modifiers type method_declarator throws
            | modifiers VOID_TOKEN method_declarator throws
        """
        return self.defaultNodeClass(
            target='method_header',
            option=option,
            names=names,
            values=values)

    def on_method_declarator(self, target, option, names, values):
        """
        method_declarator
            : identifier OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | identifier OPEN_PAREN_TOKEN formal_parameter_list CLOSE_PAREN_TOKEN
            | method_declarator OPEN_BRACKET_TOKEN CLOSE_BRACKET_TOKEN
        """
        return self.defaultNodeClass(
            target='method_declarator',
            option=option,
            names=names,
            values=values)

    def on_formal_parameter_list(self, target, option, names, values):
        """
        formal_parameter_list
            : formal_parameter
            | formal_parameter_list COMMA_TOKEN formal_parameter
        """
        return self.defaultNodeClass(
            target='formal_parameter_list',
            option=option,
            names=names,
            values=values)

    def on_formal_parameter(self, target, option, names, values):
        """
        formal_parameter
            : type variable_declarator_id
            | modifiers type variable_declarator_id
        """
        return self.defaultNodeClass(
            target='formal_parameter',
            option=option,
            names=names,
            values=values)

    def on_throws(self, target, option, names, values):
        """
        throws
            : | THROWS_TOKEN class_type_list
        """
        return self.defaultNodeClass(
            target='throws',
            option=option,
            names=names,
            values=values)

    def on_class_type_list(self, target, option, names, values):
        """
        class_type_list
            : class_type
            | class_type_list COMMA_TOKEN class_type
        """
        return self.defaultNodeClass(
            target='class_type_list',
            option=option,
            names=names,
            values=values)

    def on_method_body(self, target, option, names, values):
        """
        method_body
            : block
            | SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='method_body',
            option=option,
            names=names,
            values=values)

    def on_static_initializer(self, target, option, names, values):
        """
        static_initializer
            : static block
        """
        return self.defaultNodeClass(
            target='static_initializer',
            option=option,
            names=names,
            values=values)

    def on_static(self, target, option, names, values):
        """
        static
            : modifiers
        """
        return self.defaultNodeClass(
            target='static',
            option=option,
            names=names,
            values=values)

    def on_constructor_declaration(self, target, option, names, values):
        """
        constructor_declaration
            : constructor_header constructor_body
        """
        return self.defaultNodeClass(
            target='constructor_declaration',
            option=option,
            names=names,
            values=values)

    def on_constructor_header(self, target, option, names, values):
        """
        constructor_header
            : constructor_declarator throws
            | modifiers constructor_declarator throws
        """
        return self.defaultNodeClass(
            target='constructor_header',
            option=option,
            names=names,
            values=values)

    def on_constructor_declarator(self, target, option, names, values):
        """
        constructor_declarator
            : simple_name OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | simple_name OPEN_PAREN_TOKEN formal_parameter_list CLOSE_PAREN_TOKEN
        """
        return self.defaultNodeClass(
            target='constructor_declarator',
            option=option,
            names=names,
            values=values)

    def on_constructor_body(self, target, option, names, values):
        """
        constructor_body
            : block_begin constructor_block_end
            | block_begin explicit_constructor_invocation constructor_block_end
            | block_begin block_statements constructor_block_end
            | block_begin explicit_constructor_invocation block_statements constructor_block_end
        """
        return self.defaultNodeClass(
            target='constructor_body',
            option=option,
            names=names,
            values=values)

    def on_constructor_block_end(self, target, option, names, values):
        """
        constructor_block_end
            : block_end
        """
        return self.defaultNodeClass(
            target='constructor_block_end',
            option=option,
            names=names,
            values=values)

    def on_block_begin(self, target, option, names, values):
        """
        block_begin
            : OPEN_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='block_begin',
            option=option,
            names=names,
            values=values)

    def on_block_end(self, target, option, names, values):
        """
        block_end
            : CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='block_end',
            option=option,
            names=names,
            values=values)

    def on_explicit_constructor_invocation(self, target, option, names, values):
        """
        explicit_constructor_invocation
            : this_or_super OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN SEMICOLON_TOKEN
            | this_or_super OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN SEMICOLON_TOKEN
            | name PERIOD_TOKEN SUPER_TOKEN OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN SEMICOLON_TOKEN
            | name PERIOD_TOKEN SUPER_TOKEN OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='explicit_constructor_invocation',
            option=option,
            names=names,
            values=values)

    def on_this_or_super(self, target, option, names, values):
        """
        this_or_super
            : THIS_TOKEN
            | SUPER_TOKEN
        """
        return self.defaultNodeClass(
            target='this_or_super',
            option=option,
            names=names,
            values=values)

    def on_interface_declaration(self, target, option, names, values):
        """
        interface_declaration
            : INTERFACE_TOKEN identifier interface_body
            | modifiers INTERFACE_TOKEN identifier interface_body
            | INTERFACE_TOKEN identifier extends_interfaces interface_body
            | modifiers INTERFACE_TOKEN identifier extends_interfaces interface_body
        """
        return self.defaultNodeClass(
            target='interface_declaration',
            option=option,
            names=names,
            values=values)

    def on_extends_interfaces(self, target, option, names, values):
        """
        extends_interfaces
            : EXTENDS_TOKEN interface_type
            | extends_interfaces COMMA_TOKEN interface_type
        """
        return self.defaultNodeClass(
            target='extends_interfaces',
            option=option,
            names=names,
            values=values)

    def on_interface_body(self, target, option, names, values):
        """
        interface_body
            : OPEN_BRACE_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN interface_member_declarations CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='interface_body',
            option=option,
            names=names,
            values=values)

    def on_interface_member_declarations(self, target, option, names, values):
        """
        interface_member_declarations
            : interface_member_declaration
            | interface_member_declarations interface_member_declaration
        """
        return self.defaultNodeClass(
            target='interface_member_declarations',
            option=option,
            names=names,
            values=values)

    def on_interface_member_declaration(self, target, option, names, values):
        """
        interface_member_declaration
            : constant_declaration
            | abstract_method_declaration
            | class_declaration
            | interface_declaration
        """
        return self.defaultNodeClass(
            target='interface_member_declaration',
            option=option,
            names=names,
            values=values)

    def on_constant_declaration(self, target, option, names, values):
        """
        constant_declaration
            : field_declaration
        """
        return self.defaultNodeClass(
            target='constant_declaration',
            option=option,
            names=names,
            values=values)

    def on_abstract_method_declaration(self, target, option, names, values):
        """
        abstract_method_declaration
            : method_header SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='abstract_method_declaration',
            option=option,
            names=names,
            values=values)

    def on_array_initializer(self, target, option, names, values):
        """
        array_initializer
            : OPEN_BRACE_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN COMMA_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN variable_initializers CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN variable_initializers COMMA_TOKEN CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='array_initializer',
            option=option,
            names=names,
            values=values)

    def on_variable_initializers(self, target, option, names, values):
        """
        variable_initializers
            : variable_initializer
            | variable_initializers COMMA_TOKEN variable_initializer
        """
        return self.defaultNodeClass(
            target='variable_initializers',
            option=option,
            names=names,
            values=values)

    def on_block(self, target, option, names, values):
        """
        block
            : OPEN_BRACE_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN block_statements CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='block',
            option=option,
            names=names,
            values=values)

    def on_block_statements(self, target, option, names, values):
        """
        block_statements
            : block_statement
            | block_statements block_statement
        """
        return self.defaultNodeClass(
            target='block_statements',
            option=option,
            names=names,
            values=values)

    def on_block_statement(self, target, option, names, values):
        """
        block_statement
            : local_variable_declaration_statement
            | statement
            | class_declaration
        """
        return self.defaultNodeClass(
            target='block_statement',
            option=option,
            names=names,
            values=values)

    def on_local_variable_declaration_statement(self, target, option, names, values):
        """
        local_variable_declaration_statement
            : local_variable_declaration SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='local_variable_declaration_statement',
            option=option,
            names=names,
            values=values)

    def on_local_variable_declaration(self, target, option, names, values):
        """
        local_variable_declaration
            : type variable_declarators
            | modifiers type variable_declarators
        """
        return self.defaultNodeClass(
            target='local_variable_declaration',
            option=option,
            names=names,
            values=values)

    def on_statement(self, target, option, names, values):
        """
        statement
            : statement_without_trailing_substatement
            | labeled_statement
            | if_then_statement
            | if_then_else_statement
            | while_statement
            | for_statement
        """
        return self.defaultNodeClass(
            target='statement',
            option=option,
            names=names,
            values=values)

    def on_statement_nsi(self, target, option, names, values):
        """
        statement_nsi
            : statement_without_trailing_substatement
            | labeled_statement_nsi
            | if_then_else_statement_nsi
            | while_statement_nsi
            | for_statement_nsi
        """
        return self.defaultNodeClass(
            target='statement_nsi',
            option=option,
            names=names,
            values=values)

    def on_statement_without_trailing_substatement(self, target, option, names, values):
        """
        statement_without_trailing_substatement
            : block
            | empty_statement
            | expression_statement
            | switch_statement
            | do_statement
            | break_statement
            | continue_statement
            | return_statement
            | synchronized_statement
            | throw_statement
            | try_statement
            | assert_statement
        """
        return self.defaultNodeClass(
            target='statement_without_trailing_substatement',
            option=option,
            names=names,
            values=values)

    def on_empty_statement(self, target, option, names, values):
        """
        empty_statement
            : SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='empty_statement',
            option=option,
            names=names,
            values=values)

    def on_label_decl(self, target, option, names, values):
        """
        label_decl
            : identifier COLON_TOKEN
        """
        return self.defaultNodeClass(
            target='label_decl',
            option=option,
            names=names,
            values=values)

    def on_labeled_statement(self, target, option, names, values):
        """
        labeled_statement
            : label_decl statement
        """
        return self.defaultNodeClass(
            target='labeled_statement',
            option=option,
            names=names,
            values=values)

    def on_labeled_statement_nsi(self, target, option, names, values):
        """
        labeled_statement_nsi
            : label_decl statement_nsi
        """
        return self.defaultNodeClass(
            target='labeled_statement_nsi',
            option=option,
            names=names,
            values=values)

    def on_expression_statement(self, target, option, names, values):
        """
        expression_statement
            : statement_expression SEMICOLON_TOKEN
            | SYNCHRONIZED_TOKEN OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN block
        """
        return self.defaultNodeClass(
            target='expression_statement',
            option=option,
            names=names,
            values=values)

    def on_statement_expression(self, target, option, names, values):
        """
        statement_expression
            : assignment
            | primary
            | pre_increment_expression
            | pre_decrement_expression
            | post_increment_expression
            | post_decrement_expression
            | method_invocation
            | class_instance_creation_expression
        """
        return self.defaultNodeClass(
            target='statement_expression',
            option=option,
            names=names,
            values=values)

    def on_if_then_statement(self, target, option, names, values):
        """
        if_then_statement
            : IF_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN statement
        """
        return self.defaultNodeClass(
            target='if_then_statement',
            option=option,
            names=names,
            values=values)

    def on_if_then_else_statement(self, target, option, names, values):
        """
        if_then_else_statement
            : IF_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN statement_nsi ELSE_TOKEN statement
        """
        return self.defaultNodeClass(
            target='if_then_else_statement',
            option=option,
            names=names,
            values=values)

    def on_if_then_else_statement_nsi(self, target, option, names, values):
        """
        if_then_else_statement_nsi
            : IF_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN statement_nsi ELSE_TOKEN statement_nsi
        """
        return self.defaultNodeClass(
            target='if_then_else_statement_nsi',
            option=option,
            names=names,
            values=values)

    def on_switch_statement(self, target, option, names, values):
        """
        switch_statement
            : switch_expression switch_block
        """
        return self.defaultNodeClass(
            target='switch_statement',
            option=option,
            names=names,
            values=values)

    def on_switch_expression(self, target, option, names, values):
        """
        switch_expression
            : SWITCH_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN
        """
        return self.defaultNodeClass(
            target='switch_expression',
            option=option,
            names=names,
            values=values)

    def on_switch_block(self, target, option, names, values):
        """
        switch_block
            : OPEN_BRACE_TOKEN CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN switch_labels CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN switch_block_statement_groups CLOSE_BRACE_TOKEN
            | OPEN_BRACE_TOKEN switch_block_statement_groups switch_labels CLOSE_BRACE_TOKEN
        """
        return self.defaultNodeClass(
            target='switch_block',
            option=option,
            names=names,
            values=values)

    def on_switch_block_statement_groups(self, target, option, names, values):
        """
        switch_block_statement_groups
            : switch_block_statement_group
            | switch_block_statement_groups switch_block_statement_group
        """
        return self.defaultNodeClass(
            target='switch_block_statement_groups',
            option=option,
            names=names,
            values=values)

    def on_switch_block_statement_group(self, target, option, names, values):
        """
        switch_block_statement_group
            : switch_labels block_statements
        """
        return self.defaultNodeClass(
            target='switch_block_statement_group',
            option=option,
            names=names,
            values=values)

    def on_switch_labels(self, target, option, names, values):
        """
        switch_labels
            : switch_label
            | switch_labels switch_label
        """
        return self.defaultNodeClass(
            target='switch_labels',
            option=option,
            names=names,
            values=values)

    def on_switch_label(self, target, option, names, values):
        """
        switch_label
            : CASE_TOKEN constant_expression COLON_TOKEN
            | DEFAULT_TOKEN COLON_TOKEN
        """
        return self.defaultNodeClass(
            target='switch_label',
            option=option,
            names=names,
            values=values)

    def on_while_expression(self, target, option, names, values):
        """
        while_expression
            : WHILE_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN
        """
        return self.defaultNodeClass(
            target='while_expression',
            option=option,
            names=names,
            values=values)

    def on_while_statement(self, target, option, names, values):
        """
        while_statement
            : while_expression statement
        """
        return self.defaultNodeClass(
            target='while_statement',
            option=option,
            names=names,
            values=values)

    def on_while_statement_nsi(self, target, option, names, values):
        """
        while_statement_nsi
            : while_expression statement_nsi
        """
        return self.defaultNodeClass(
            target='while_statement_nsi',
            option=option,
            names=names,
            values=values)

    def on_do_statement_begin(self, target, option, names, values):
        """
        do_statement_begin
            : DO_TOKEN
        """
        return self.defaultNodeClass(
            target='do_statement_begin',
            option=option,
            names=names,
            values=values)

    def on_do_statement(self, target, option, names, values):
        """
        do_statement
            : do_statement_begin statement WHILE_TOKEN OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='do_statement',
            option=option,
            names=names,
            values=values)

    def on_for_statement(self, target, option, names, values):
        """
        for_statement
            : for_begin SEMICOLON_TOKEN expression SEMICOLON_TOKEN for_update CLOSE_PAREN_TOKEN statement
            | for_begin SEMICOLON_TOKEN SEMICOLON_TOKEN for_update CLOSE_PAREN_TOKEN statement
        """
        return self.defaultNodeClass(
            target='for_statement',
            option=option,
            names=names,
            values=values)

    def on_for_statement_nsi(self, target, option, names, values):
        """
        for_statement_nsi
            : for_begin SEMICOLON_TOKEN expression SEMICOLON_TOKEN for_update CLOSE_PAREN_TOKEN statement_nsi
            | for_begin SEMICOLON_TOKEN SEMICOLON_TOKEN for_update CLOSE_PAREN_TOKEN statement_nsi
        """
        return self.defaultNodeClass(
            target='for_statement_nsi',
            option=option,
            names=names,
            values=values)

    def on_for_header(self, target, option, names, values):
        """
        for_header
            : FOR_TOKEN OPEN_PAREN_TOKEN
        """
        return self.defaultNodeClass(
            target='for_header',
            option=option,
            names=names,
            values=values)

    def on_for_begin(self, target, option, names, values):
        """
        for_begin
            : for_header for_init
        """
        return self.defaultNodeClass(
            target='for_begin',
            option=option,
            names=names,
            values=values)

    def on_for_init(self, target, option, names, values):
        """
        for_init
            : | statement_expression_list
            | local_variable_declaration
        """
        return self.defaultNodeClass(
            target='for_init',
            option=option,
            names=names,
            values=values)

    def on_for_update(self, target, option, names, values):
        """
        for_update
            : | statement_expression_list
        """
        return self.defaultNodeClass(
            target='for_update',
            option=option,
            names=names,
            values=values)

    def on_statement_expression_list(self, target, option, names, values):
        """
        statement_expression_list
            : statement_expression
            | statement_expression_list COMMA_TOKEN statement_expression
        """
        return self.defaultNodeClass(
            target='statement_expression_list',
            option=option,
            names=names,
            values=values)

    def on_break_statement(self, target, option, names, values):
        """
        break_statement
            : BREAK_TOKEN SEMICOLON_TOKEN
            | BREAK_TOKEN identifier SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='break_statement',
            option=option,
            names=names,
            values=values)

    def on_continue_statement(self, target, option, names, values):
        """
        continue_statement
            : CONTINUE_TOKEN SEMICOLON_TOKEN
            | CONTINUE_TOKEN identifier SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='continue_statement',
            option=option,
            names=names,
            values=values)

    def on_return_statement(self, target, option, names, values):
        """
        return_statement
            : RETURN_TOKEN SEMICOLON_TOKEN
            | RETURN_TOKEN expression SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='return_statement',
            option=option,
            names=names,
            values=values)

    def on_throw_statement(self, target, option, names, values):
        """
        throw_statement
            : THROW_TOKEN expression SEMICOLON_TOKEN
        """
        return self.defaultNodeClass(
            target='throw_statement',
            option=option,
            names=names,
            values=values)

    def on_assert_statement(self, target, option, names, values):
        """
        assert_statement
            : ASSERT_TOKEN expression COLON_TOKEN expression SEMICOLON_TOKEN
            | ASSERT_TOKEN expression SEMICOLON_TOKEN
            | ASSERT_TOKEN error
            | ASSERT_TOKEN expression error
        """
        return self.defaultNodeClass(
            target='assert_statement',
            option=option,
            names=names,
            values=values)

    def on_synchronized_statement(self, target, option, names, values):
        """
        synchronized_statement
            : synchronized OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN block
            | synchronized OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN error
        """
        return self.defaultNodeClass(
            target='synchronized_statement',
            option=option,
            names=names,
            values=values)

    def on_synchronized(self, target, option, names, values):
        """
        synchronized
            : MODIFIER_TOKEN
        """
        return self.defaultNodeClass(
            target='synchronized',
            option=option,
            names=names,
            values=values)

    def on_try_statement(self, target, option, names, values):
        """
        try_statement
            : TRY_TOKEN block catches
            | TRY_TOKEN block finally
            | TRY_TOKEN block catches finally
        """
        return self.defaultNodeClass(
            target='try_statement',
            option=option,
            names=names,
            values=values)

    def on_catches(self, target, option, names, values):
        """
        catches
            : catch_clause
            | catches catch_clause
        """
        return self.defaultNodeClass(
            target='catches',
            option=option,
            names=names,
            values=values)

    def on_catch_clause(self, target, option, names, values):
        """
        catch_clause
            : CATCH_TOKEN OPEN_PAREN_TOKEN formal_parameter CLOSE_PAREN_TOKEN block
        """
        return self.defaultNodeClass(
            target='catch_clause',
            option=option,
            names=names,
            values=values)

    def on_finally(self, target, option, names, values):
        """
        finally
            : FINALLY_TOKEN block
        """
        return self.defaultNodeClass(
            target='finally',
            option=option,
            names=names,
            values=values)

    def on_primary(self, target, option, names, values):
        """
        primary
            : primary_no_new_array
            | array_creation_expression
        """
        return self.defaultNodeClass(
            target='primary',
            option=option,
            names=names,
            values=values)

    def on_primary_no_new_array(self, target, option, names, values):
        """
        primary_no_new_array
            : literal
            | THIS_TOKEN
            | OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN
            | class_instance_creation_expression
            | field_access
            | method_invocation
            | array_access
            | type_literals
            | name PERIOD_TOKEN THIS_TOKEN
        """
        return self.defaultNodeClass(
            target='primary_no_new_array',
            option=option,
            names=names,
            values=values)

    def on_type_literals(self, target, option, names, values):
        """
        type_literals
            : name PERIOD_TOKEN CLASS_TOKEN
            | array_type PERIOD_TOKEN CLASS_TOKEN
            | primitive_type PERIOD_TOKEN CLASS_TOKEN
            | VOID_TOKEN PERIOD_TOKEN CLASS_TOKEN
        """
        return self.defaultNodeClass(
            target='type_literals',
            option=option,
            names=names,
            values=values)

    def on_class_instance_creation_expression(self, target, option, names, values):
        """
        class_instance_creation_expression
            : NEW_TOKEN class_type OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN
            | NEW_TOKEN class_type OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | anonymous_class_creation
            | something_dot_new identifier OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | something_dot_new identifier OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN class_body
            | something_dot_new identifier OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN
            | something_dot_new identifier OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN class_body
        """
        return self.defaultNodeClass(
            target='class_instance_creation_expression',
            option=option,
            names=names,
            values=values)

    def on_anonymous_class_creation(self, target, option, names, values):
        """
        anonymous_class_creation
            : NEW_TOKEN class_type OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN class_body
            | NEW_TOKEN class_type OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN class_body
        """
        return self.defaultNodeClass(
            target='anonymous_class_creation',
            option=option,
            names=names,
            values=values)

    def on_something_dot_new(self, target, option, names, values):
        """
        something_dot_new
            : name PERIOD_TOKEN NEW_TOKEN
            | primary PERIOD_TOKEN NEW_TOKEN
        """
        return self.defaultNodeClass(
            target='something_dot_new',
            option=option,
            names=names,
            values=values)

    def on_argument_list(self, target, option, names, values):
        """
        argument_list
            : expression
            | argument_list COMMA_TOKEN expression
            | argument_list COMMA_TOKEN error
        """
        return self.defaultNodeClass(
            target='argument_list',
            option=option,
            names=names,
            values=values)

    def on_array_creation_expression(self, target, option, names, values):
        """
        array_creation_expression
            : NEW_TOKEN primitive_type dim_exprs
            | NEW_TOKEN class_or_interface_type dim_exprs
            | NEW_TOKEN primitive_type dim_exprs dims
            | NEW_TOKEN class_or_interface_type dim_exprs dims
            | NEW_TOKEN class_or_interface_type dims array_initializer
            | NEW_TOKEN primitive_type dims array_initializer
        """
        return self.defaultNodeClass(
            target='array_creation_expression',
            option=option,
            names=names,
            values=values)

    def on_dim_exprs(self, target, option, names, values):
        """
        dim_exprs
            : dim_expr
            | dim_exprs dim_expr
        """
        return self.defaultNodeClass(
            target='dim_exprs',
            option=option,
            names=names,
            values=values)

    def on_dim_expr(self, target, option, names, values):
        """
        dim_expr
            : OPEN_BRACKET_TOKEN expression CLOSE_BRACKET_TOKEN
        """
        return self.defaultNodeClass(
            target='dim_expr',
            option=option,
            names=names,
            values=values)

    def on_dims(self, target, option, names, values):
        """
        dims
            : OPEN_BRACKET_TOKEN CLOSE_BRACKET_TOKEN
            | dims OPEN_BRACKET_TOKEN CLOSE_BRACKET_TOKEN
        """
        return self.defaultNodeClass(
            target='dims',
            option=option,
            names=names,
            values=values)

    def on_field_access(self, target, option, names, values):
        """
        field_access
            : primary PERIOD_TOKEN identifier
            | SUPER_TOKEN PERIOD_TOKEN identifier
        """
        return self.defaultNodeClass(
            target='field_access',
            option=option,
            names=names,
            values=values)

    def on_method_invocation(self, target, option, names, values):
        """
        method_invocation
            : name OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | name OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN
            | primary PERIOD_TOKEN identifier OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | primary PERIOD_TOKEN identifier OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN
            | SUPER_TOKEN PERIOD_TOKEN identifier OPEN_PAREN_TOKEN CLOSE_PAREN_TOKEN
            | SUPER_TOKEN PERIOD_TOKEN identifier OPEN_PAREN_TOKEN argument_list CLOSE_PAREN_TOKEN
        """
        return self.defaultNodeClass(
            target='method_invocation',
            option=option,
            names=names,
            values=values)

    def on_array_access(self, target, option, names, values):
        """
        array_access
            : name OPEN_BRACKET_TOKEN expression CLOSE_BRACKET_TOKEN
            | primary_no_new_array OPEN_BRACKET_TOKEN expression CLOSE_BRACKET_TOKEN
        """
        return self.defaultNodeClass(
            target='array_access',
            option=option,
            names=names,
            values=values)

    def on_postfix_expression(self, target, option, names, values):
        """
        postfix_expression
            : primary
            | name
            | post_increment_expression
            | post_decrement_expression
        """
        return self.defaultNodeClass(
            target='postfix_expression',
            option=option,
            names=names,
            values=values)

    def on_post_increment_expression(self, target, option, names, values):
        """
        post_increment_expression
            : postfix_expression INC_TOKEN
        """
        return self.defaultNodeClass(
            target='post_increment_expression',
            option=option,
            names=names,
            values=values)

    def on_post_decrement_expression(self, target, option, names, values):
        """
        post_decrement_expression
            : postfix_expression DEC_TOKEN
        """
        return self.defaultNodeClass(
            target='post_decrement_expression',
            option=option,
            names=names,
            values=values)

    def on_trap_overflow_corner_case(self, target, option, names, values):
        """
        trap_overflow_corner_case
            : pre_increment_expression
            | pre_decrement_expression
            | PLUS_TOKEN unary_expression
            | unary_expression_not_plus_minus
        """
        return self.defaultNodeClass(
            target='trap_overflow_corner_case',
            option=option,
            names=names,
            values=values)

    def on_unary_expression(self, target, option, names, values):
        """
        unary_expression
            : trap_overflow_corner_case
            | MINUS_TOKEN trap_overflow_corner_case
            | MINUS_TOKEN error
        """
        return self.defaultNodeClass(
            target='unary_expression',
            option=option,
            names=names,
            values=values)

    def on_pre_increment_expression(self, target, option, names, values):
        """
        pre_increment_expression
            : INC_TOKEN unary_expression
        """
        return self.defaultNodeClass(
            target='pre_increment_expression',
            option=option,
            names=names,
            values=values)

    def on_pre_decrement_expression(self, target, option, names, values):
        """
        pre_decrement_expression
            : DEC_TOKEN unary_expression
        """
        return self.defaultNodeClass(
            target='pre_decrement_expression',
            option=option,
            names=names,
            values=values)

    def on_unary_expression_not_plus_minus(self, target, option, names, values):
        """
        unary_expression_not_plus_minus
            : postfix_expression
            | TILDE_TOKEN unary_expression
            | NOT_TOKEN unary_expression
            | cast_expression
        """
        return self.defaultNodeClass(
            target='unary_expression_not_plus_minus',
            option=option,
            names=names,
            values=values)

    def on_cast_expression(self, target, option, names, values):
        """
        cast_expression
            : OPEN_PAREN_TOKEN primitive_type dims CLOSE_PAREN_TOKEN unary_expression
            | OPEN_PAREN_TOKEN primitive_type CLOSE_PAREN_TOKEN unary_expression
            | OPEN_PAREN_TOKEN expression CLOSE_PAREN_TOKEN unary_expression_not_plus_minus
            | OPEN_PAREN_TOKEN name dims CLOSE_PAREN_TOKEN unary_expression_not_plus_minus
        """
        return self.defaultNodeClass(
            target='cast_expression',
            option=option,
            names=names,
            values=values)

    def on_multiplicative_expression(self, target, option, names, values):
        """
        multiplicative_expression
            : unary_expression
            | multiplicative_expression MUL_TOKEN unary_expression
            | multiplicative_expression DIV_TOKEN unary_expression
            | multiplicative_expression MOD_TOKEN unary_expression
        """
        return self.defaultNodeClass(
            target='multiplicative_expression',
            option=option,
            names=names,
            values=values)

    def on_additive_expression(self, target, option, names, values):
        """
        additive_expression
            : multiplicative_expression
            | additive_expression PLUS_TOKEN multiplicative_expression
            | additive_expression MINUS_TOKEN multiplicative_expression
        """
        return self.defaultNodeClass(
            target='additive_expression',
            option=option,
            names=names,
            values=values)

    def on_shift_expression(self, target, option, names, values):
        """
        shift_expression
            : additive_expression
            | shift_expression SHL_TOKEN additive_expression
            | shift_expression SHR_TOKEN additive_expression
            | shift_expression SAR_TOKEN additive_expression
        """
        return self.defaultNodeClass(
            target='shift_expression',
            option=option,
            names=names,
            values=values)

    def on_relational_expression(self, target, option, names, values):
        """
        relational_expression
            : shift_expression
            | relational_expression LESS_TOKEN shift_expression
            | relational_expression GREATER_TOKEN shift_expression
            | relational_expression LE_TOKEN shift_expression
            | relational_expression GE_TOKEN shift_expression
            | relational_expression INSTANCEOF_TOKEN reference_type
        """
        return self.defaultNodeClass(
            target='relational_expression',
            option=option,
            names=names,
            values=values)

    def on_equality_expression(self, target, option, names, values):
        """
        equality_expression
            : relational_expression
            | equality_expression EQ_TOKEN relational_expression
            | equality_expression NE_OP_TOKEN relational_expression
        """
        return self.defaultNodeClass(
            target='equality_expression',
            option=option,
            names=names,
            values=values)

    def on_and_expression(self, target, option, names, values):
        """
        and_expression
            : equality_expression
            | and_expression AND_TOKEN equality_expression
        """
        return self.defaultNodeClass(
            target='and_expression',
            option=option,
            names=names,
            values=values)

    def on_exclusive_or_expression(self, target, option, names, values):
        """
        exclusive_or_expression
            : and_expression
            | exclusive_or_expression XOR_TOKEN and_expression
        """
        return self.defaultNodeClass(
            target='exclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_inclusive_or_expression(self, target, option, names, values):
        """
        inclusive_or_expression
            : exclusive_or_expression
            | inclusive_or_expression OR_TOKEN exclusive_or_expression
        """
        return self.defaultNodeClass(
            target='inclusive_or_expression',
            option=option,
            names=names,
            values=values)

    def on_conditional_and_expression(self, target, option, names, values):
        """
        conditional_and_expression
            : inclusive_or_expression
            | conditional_and_expression LOGICAL_AND_TOKEN inclusive_or_expression
        """
        return self.defaultNodeClass(
            target='conditional_and_expression',
            option=option,
            names=names,
            values=values)

    def on_conditional_or_expression(self, target, option, names, values):
        """
        conditional_or_expression
            : conditional_and_expression
            | conditional_or_expression LOGICAL_OR_TOKEN conditional_and_expression
        """
        return self.defaultNodeClass(
            target='conditional_or_expression',
            option=option,
            names=names,
            values=values)

    def on_conditional_expression(self, target, option, names, values):
        """
        conditional_expression
            : conditional_or_expression
            | conditional_or_expression CONDITIONAL_TOKEN expression COLON_TOKEN conditional_expression
        """
        return self.defaultNodeClass(
            target='conditional_expression',
            option=option,
            names=names,
            values=values)

    def on_assignment_expression(self, target, option, names, values):
        """
        assignment_expression
            : conditional_expression
            | assignment
        """
        return self.defaultNodeClass(
            target='assignment_expression',
            option=option,
            names=names,
            values=values)

    def on_assignment(self, target, option, names, values):
        """
        assignment
            : left_hand_side assignment_operator assignment_expression
        """
        return self.defaultNodeClass(
            target='assignment',
            option=option,
            names=names,
            values=values)

    def on_left_hand_side(self, target, option, names, values):
        """
        left_hand_side
            : name
            | field_access
            | array_access
        """
        return self.defaultNodeClass(
            target='left_hand_side',
            option=option,
            names=names,
            values=values)

    def on_assignment_operator(self, target, option, names, values):
        """
        assignment_operator
            : ASSIGNS_TOKEN
            | ADD_ASSIGN_TOKEN
            | SUB_ASSIGN_TOKEN
            | MUL_ASSIGN_TOKEN
            | DIV_ASSIGN_TOKEN
            | MOD_ASSIGN_TOKEN
            | SHL_ASSIGN_TOKEN
            | SHR_ASSIGN_TOKEN
            | SAR_ASSIGN_TOKEN
            | AND_ASSIGN_TOKEN
            | XOR_ASSIGN_TOKEN
            | OR_ASSIGN_TOKEN
        """
        return self.defaultNodeClass(
            target='assignment_operator',
            option=option,
            names=names,
            values=values)

    def on_expression(self, target, option, names, values):
        """
        expression
            : assignment_expression
        """
        return self.defaultNodeClass(
            target='expression',
            option=option,
            names=names,
            values=values)

    def on_constant_expression(self, target, option, names, values):
        """
        constant_expression
            : expression
        """
        return self.defaultNodeClass(
            target='constant_expression',
            option=option,
            names=names,
            values=values)

    # -----------------------------------------
    # raw lex script, verbatim here
    # -----------------------------------------
    lexscript = r"""
D            [0-9]
N            [1-9]
L            [a-zA-Z_$]
H            [a-fA-F0-9]
OC           [0-7]
E            [Ee][+-]?{D}+
LS           [fFdD]
Escape       \\[ntbrf\\'"]
Escchar      \\{D}({D}?{D})?
Escunichar   \\u{H}{H}{H}{H}

%{
//int yylineno = 0;
#include <stdio.h>
#include <string.h>
#include "Python.h"
#include "tmp.tab.h"
extern void *py_parser;
extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
#define returntoken(tok) /*printf("%d=%s\n", tok, yytext);*/ yylval = PyUnicode_FromString(strdup(yytext)); return (tok);
#define YY_INPUT(buf,result,max_size) { (*py_input)(py_parser, buf, &result, max_size); }

#include "table.h"
void comment();
void commentold();

%}

%%


{N}{D}*(l|L)?           { returntoken(INTEGER_LITERAL_TOKEN); }
{N}{D}*(d|D)?           { returntoken(INTEGER_LITERAL_TOKEN); }
0[xX]{H}+(l|L)?         { returntoken(INTEGER_LITERAL_TOKEN); }
0{OC}*(l|L)?            { returntoken(INTEGER_LITERAL_TOKEN); }

{D}+"."{D}*({E})?{LS}?  { returntoken(FLOATING_POINT_LITERAL_TOKEN); }
"."{D}+({E})?{LS}?      { returntoken(FLOATING_POINT_LITERAL_TOKEN); }
{D}+{E}{LS}?            { returntoken(FLOATING_POINT_LITERAL_TOKEN); }
{D}{LS}                 { returntoken(FLOATING_POINT_LITERAL_TOKEN); }


"true"                  { returntoken(BOOLEAN_LITERAL_TOKEN); }
"false"                 { returntoken(BOOLEAN_LITERAL_TOKEN); }

{L}({L}|{D})*           { returntoken(Table_Lookup(KeywordTable));}

'[^'\\]'                { returntoken(CHARACTER_LITERAL_TOKEN);}
'{Escape}'              { returntoken(CHARACTER_LITERAL_TOKEN);}


  \"([^\"\\]|{Escape}|{Escchar}|{Escunichar})*\" { returntoken(STRING_LITERAL_TOKEN); }

\/\/.*$                 {}
\/\*                    { comment();}

"("     { returntoken(OPEN_PAREN_TOKEN); }
")"     { returntoken(CLOSE_PAREN_TOKEN); }
"{"     { returntoken(OPEN_BRACE_TOKEN); }
"}"     { returntoken(CLOSE_BRACE_TOKEN); }
"["     { returntoken(OPEN_BRACKET_TOKEN); }
"]"     { returntoken(CLOSE_BRACKET_TOKEN); }
";"     { returntoken(SEMICOLON_TOKEN); }
","     { returntoken(COMMA_TOKEN); }
"."     { returntoken(PERIOD_TOKEN); }
"="     { returntoken(ASSIGNS_TOKEN); }
">"     { returntoken(GREATER_TOKEN); }
"<"     { returntoken(LESS_TOKEN); }
"!"     { returntoken(NOT_TOKEN); }
"~"     { returntoken(TILDE_TOKEN); }
"?"     { returntoken(CONDITIONAL_TOKEN); }
":"     { returntoken(COLON_TOKEN); }
"=="    { returntoken(EQ_TOKEN); }
"<="    { returntoken(LE_TOKEN); }
">="    { returntoken(GE_TOKEN); }
"!="    { returntoken(NE_OP_TOKEN); }
"||"    { returntoken(LOGICAL_OR_TOKEN); }
"&&"    { returntoken(LOGICAL_AND_TOKEN); }
"++"    { returntoken(INC_TOKEN); }
"--"    { returntoken(DEC_TOKEN); }
"+"     { returntoken(PLUS_TOKEN); }
"-"     { returntoken(MINUS_TOKEN); }
"*"     { returntoken(MUL_TOKEN); }
"/"     { returntoken(DIV_TOKEN); }
"&"     { returntoken(AND_TOKEN); }
"|"     { returntoken(OR_TOKEN); }
"^"     { returntoken(XOR_TOKEN); }
"%"     { returntoken(MOD_TOKEN); }
"<<"    { returntoken(SHL_TOKEN); }
">>"    { returntoken(SAR_TOKEN); }
">>>"   { returntoken(SHL_TOKEN); }
"+="    { returntoken(ADD_ASSIGN_TOKEN); }
"-="    { returntoken(SUB_ASSIGN_TOKEN); }
"*="    { returntoken(MUL_ASSIGN_TOKEN); }
"/="    { returntoken(DIV_ASSIGN_TOKEN); }
"&="    { returntoken(AND_ASSIGN_TOKEN); }
"|="    { returntoken(OR_ASSIGN_TOKEN); }
"^="    { returntoken(XOR_ASSIGN_TOKEN); }
"%="    { returntoken(MOD_ASSIGN_TOKEN); }
"<<="   { returntoken(SHL_ASSIGN_TOKEN); }
">>="   { returntoken(SAR_ASSIGN_TOKEN); }
">>>="  { returntoken(SHR_ASSIGN_TOKEN); }

[ \t\v\f]             {}
[\n]            {yylineno++;}

.       { printf("unknown char %c ignored\n", yytext[0]); /* ignore bad chars */}


%%

yywrap() { return(1); }

/* test_main()
{
    int t;

    for(t = yylex(), t > 0, t = yylex())
    {
        printf("%s\t%d\n", yytext,t);
    }

    return 0;
}
*/


/* input: Table of tokens
 * returns TokenCode of keyword if matched or
 * ID_TOKEN if no match is found
 */
int Table_Lookup(struct KeywordToken Table[])
{
    struct KeywordToken *Curr;
    int i = 0;

    for (Curr = Table; Curr->Keyword != ""; Curr++)
      {
        //printf("Table_Lookup: yytext='%s', Curr->Keyword='%s', idx=%d\n", yytext, Curr->Keyword, i);

        if (strcmp(Curr->Keyword, yytext)==0)
          {
            //printf("Table_Lookup: '%s' => %d\n", yytext, Curr->TokenCode);
            return (Curr->TokenCode);
          }
        i++;
      }
    return ID_TOKEN;
}

void commentold()
{
    char c = -1, c1;
    while(c != 0)
    {
        for(c = input(); c != '*' && c!=0; c = input())
            ;

        /* now we have a star or no more chars */
        if(c == 0 || (c1 = input() == '/'))
            return;

        if (c1 == '*')
            unput(c1);
    }
}

void comment()
{
  int prev=-1, cur=-1;

  while (1)
    {
      cur = input();
      if (cur == '/' && prev == '*')
        return;
      else if (cur == 0)
        return;
      prev = cur;
    }
}

    """
    # -----------------------------------------
    # end raw lex script
    # -----------------------------------------


def main():
    import argparse
    parser = argparse.ArgumentParser(prog=f"PyBison Java Example (derived from {bisonFile} and {lexFile})")
    parser.add_argument("-k", "--keepfiles", action="store_true",
                        help="Keep temporary files used in building parse engine lib")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose messages while parser is running")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable garrulous debug messages from parser engine")
    parser.add_argument("filename", type=str, nargs="*",
                        help="path of a file to parse, defaults to stdin")
    args = parser.parse_args()
    # replace default value with None
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
