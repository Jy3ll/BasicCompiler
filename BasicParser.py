import ply.yacc as yacc
import BasicLexer
tokens=BasicLexer.tokens

precedence = (
    ('nonassoc','LESS_THAN','MORE_THAN','LESS_OR_EQUAL','MORE_OR_EQUAL','EQUAL','NOT_EQUAL'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS')
)
start = 'stmt'

def p_expr_plus(p):
    'expr : expr PLUS term'
    p[0]=('+',p[1],p[3])

def p_expr_minus(p):
    'expr : expr MINUS term'
    p[0]=('-',p[1],p[3])

def p_expr_term(p):
    'expr : term'
    p[0]=p[1]

def p_term_times(p):
    'term: term TIMES factor'
    p[0]=('*',p[1],p[3])

def p_term_divide(p):
    'term: term DIVIDE factor'
    p[0]=('/',p[1],p[3])

def p_term_mod(p):
    'term: term MOD term'
    p[0]=('mod',p[1],p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_int(p):
    'factor : INTEGER'
    p[0]=p[1]

def p_factor_float(p):
    'factor : FLOAT'
    p[0]=p[1]

def p_factor_uminus(p):
    'factor : MINUS factor %prec UMINUS'
    p[0]=-p[1]

def p_factor_expr(p):
    'factor : LPAR expr RPAR'
    p[0]=('()',p[2])

def p_assign_expr(p):
    'assign : ID ASSIGN expr'
    p[0]=(':=',p[1],p[3])

def p_assign_str(p):
    'assign : ID ASSIGN STRING'
    p[0]=(':=',p[1],p[3])

def p_assign_lfactor(p):
    'assign : ID ASSIGN lfactor'
    p[0]=(':=',p[1],p[3])

def p_lexpr_less(p):
    'lexpr : factor LESS_THAN factor'
    p[0]=('<',p[1],p[3])

def p_lexpr_more(p):
    'lexpr : factor MORE_THAN factor'
    p[0]=('>',p[1],p[3])

def p_lexpr_less_or_eq(p):
    'lexpr : factor LESS_OR_EQUAL factor'
    p[0]=('<=',p[1],p[3])

def p_lexpr_more_or_eq(p):
    'lexpr : factor MORE_OR_EQUAL factor'
    p[0]=('>=',p[1],p[3])

def p_lexpr_eq(p):
    'lexpr : factor EQUAL factor'
    p[0]=('==',p[1],p[3])

def p_lexpr_eq_string(p):
    'lexpr : STRING EQUAL STRING'
    p[0] = ('==', p[1], p[3])

def p_lexpr_not_eq(p):
    'lexpr : factor NOT_EQUAL factor'
    p[0]=('<>',p[1],p[3])

def p_lexpr_and(p):
    'lexpr : lfactor AND lfactor'
    p[0]=('and',p[2],p[6])

def p_lexpr_or(p):
    'lexpr : lfactor OR lfactor'
    p[0]=('or',p[2],p[6])

def p_lexpr_xor(p):
    'lexpr : lfactor XOR lfactor'
    p[0]=('xor',p[2],p[6])

def p_lexpr_not(p):
    'lexpr : NOT lfactor'
    p[0]=('not',p[3])

def p_lfactor_true(p):
    'lfactor : TRUE'
    p[0] = p[1]

def p_lfactor_false(p):
    'lfactor : FALSE'
    p[0] = p[1]

def p_lfactor_lexpr(p):
    'lfactor : LPAR lexpr RPAR'
    p[0] = ('()',p[2])

def p_if_stmt(p):
    'if_stmt : IF lexpr THEN stmt END IF'
    p[0]=('if',p[1],p[4])

def p_if_stmt_else(p):
    'if_stmt : IF lexpr THEN stmt ELSE stmt END IF'
    p[0]=('if_else',p[1],p[4],p[6])

def p_while_stmt(p):
    'while_stmt : WHILE lexpr DO loop_stmt END WHILE'
    p[0]=('while',p[1],p[4])

def p_loop_stmt_cont(p):
    'loop_stmt : CONTINUE'
    p[0]=p[1]

def p_loop_stmt_br(p):
    'loop_stmt : BREAK'
    p[0]=p[1]

def p_loop_stmt(p):
    'loop_stmt : loop_stmt stmt'





def p_error(p):
    print("Syntax error!")

parser=yacc.yacc()