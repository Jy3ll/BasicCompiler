import ply.lex as lex

reserved = {
    'and': 'AND',
    'AND': 'AND',
    'not': 'NOT',
    'NOT': 'NOT',
    'or': 'OR',
    'OR': 'OR',
    'xor': 'XOR',
    'XOR': 'XOR',
    'while': 'WHILE',
    'WHILE': 'WHILE',
    'mod': 'MOD',
    'MOD': 'MOD',
    'if': 'IF',
    'IF': 'IF',
    'else': 'ELSE',
    'ELSE': 'ELSE',
    'continue': 'CONTINUE',
    'CONTINUE': 'CONTINUE',
    'exit': 'EXIT',
    'EXIT': 'EXIT',
    'end': 'END',
    'END': 'END',
    'then': 'THEN',
    'THEN': 'THEN',
    'true': 'TRUE',
    'TRUE': 'TRUE',
    'false': 'FALSE',
    'FALSE': 'FALSE',
    'print': 'PRINT',
    'PRINT': 'PRINT',
    'function': 'FUNCTION',
    'FUNCTION': 'FUNCTION',
    'return': 'RETURN',
    'RETURN': 'RETURN',
    'do':'DO',
    'DO':'DO'
}

tokens = ['ID', 'INTEGER', 'FLOAT', 'STRING', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUAL', 'LESS_THAN',
          'MORE_THAN',
          'LESS_OR_EQUAL', 'MORE_OR_EQUAL', 'NOT_EQUAL', 'LPAR', 'RPAR', 'COMMA'] + list(
    dict.fromkeys(list(reserved.values())))

t_ignore = ' \t'
t_ignore_COMMENT=r'\'.*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'=='
t_COMMA = ','
t_ASSIGN = r'='
t_LESS_THAN = r'<'
t_MORE_THAN = r'>'
t_LESS_OR_EQUAL = r'<='
t_MORE_OR_EQUAL = r'>='
t_NOT_EQUAL = r'<>'
t_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_LPAR = r'\('
t_RPAR = r'\)'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)

    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
