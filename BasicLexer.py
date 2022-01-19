import ply.lex as lex
tokens = ['ID','INTEGER','FLOAT','STRING','ASSIGN','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LESS_THAN','MORE_THAN',
          'LESS_OR_EQUAL','MORE_OR_EQUAL','NOT_EQUAL','LPAR','RPAR','NOT','AND','OR','WHILE','XOR','MOD','IF','ELSE',
          'CONTINUE','EXIT','PROCEDURE','END','THEN','TRUE','FALSE','PRINT','DO']
t_ignore=' \t'
t_PLUS=r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'=='
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN= r':='
t_LESS_THAN = r'<'
t_MORE_THAN = r'>'
t_LESS_OR_EQUAL = r'<='
t_MORE_OR_EQUAL = r'>='
t_NOT_EQUAL= r'<>'
t_NOT=r'not'
t_AND=r'and'
t_OR=r'or'
t_WHILE=r'while'
t_XOR=r'xor'
t_MOD=r'mod'
t_IF=r'if'
t_ELSE=r'else'
t_CONTINUE=r'continue'
t_EXIT=r'exit'
t_PROCEDURE=r'procedure'
t_END=r'end'
t_THEN=r'then'
t_STRING=r'".*"'
t_LPAR=r'('
t_RPAR=r')'
t_TRUE=r'true'
t_FALSE=r'false'
t_PRINT=r'print'
t_DO=r'do'

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)

    return t
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)

lexer=lex.lex()