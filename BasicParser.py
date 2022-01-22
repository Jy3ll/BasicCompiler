import ply.yacc as yacc
import BasicLexer
tokens=BasicLexer.tokens

precedence = (
    ('nonassoc','RETURNX'),
    ('nonassoc', 'ID'),
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('nonassoc','LESS_THAN','MORE_THAN','LESS_OR_EQUAL','MORE_OR_EQUAL','EQUAL','NOT_EQUAL'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MOD'),
    ('right','UMINUS'),
    ('right','ASSIGN')
)
start = 'prog'
def p_prog(p):
    '''prog : stmt_block'''
    p[0]=p[1]

def p_expr_plus(p):
    '''expr : expr PLUS term'''
    p[0]=('+',p[1],p[3])

def p_expr_minus(p):
    '''expr : expr MINUS term'''
    p[0]=('-',p[1],p[3])

def p_expr_term(p):
    '''expr : term'''
    p[0]=p[1]

def p_term_times(p):
    '''term : term TIMES factor'''
    p[0]=('*',p[1],p[3])

def p_term_divide(p):
    '''term : term DIVIDE factor'''
    p[0]=('/',p[1],p[3])

def p_term_mod(p):
    '''term : term MOD term'''
    p[0]=('mod',p[1],p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_int(p):
    '''factor : INTEGER'''
    p[0]=p[1]

def p_factor_float(p):
    '''factor : FLOAT'''
    p[0]=p[1]

def p_factor_id(p):
    '''factor : ID'''
    p[0]=p[1]

def p_factor_call(p):
    '''factor : func_call_stmt'''
    p[0]=p[1]
def p_factor_uminus(p):
    '''factor : MINUS factor %prec UMINUS'''
    p[0]=("uminus",p[2])

def p_factor_expr(p):
    '''factor : LPAR expr RPAR'''
    p[0]=('()',p[2])

def p_assign_expr(p):
    '''assign : ID ASSIGN expr'''
    p[0]=(':=',p[1],p[3])

def p_assign_str(p):
    '''assign : ID ASSIGN STRING'''
    p[0]=(':=',p[1],p[3])

def p_assign_lexpr(p):
    '''assign : ID ASSIGN lexpr'''
    p[0]=(':=',p[1],p[3])

def p_lexpr_less(p):
    '''lexpr : factor LESS_THAN factor'''
    p[0]=('<',p[1],p[3])

def p_lexpr_more(p):
    '''lexpr : factor MORE_THAN factor'''
    p[0]=('>',p[1],p[3])

def p_lexpr_less_or_eq(p):
    '''lexpr : factor LESS_OR_EQUAL factor'''
    p[0]=('<=',p[1],p[3])

def p_lexpr_more_or_eq(p):
    '''lexpr : factor MORE_OR_EQUAL factor'''
    p[0]=('>=',p[1],p[3])

def p_lexpr_eq_factor(p):
    '''lexpr : factor EQUAL factor'''
    p[0]=('==',p[1],p[3])

def p_plexpr_eq_factor(p):
    '''lexpr : lfactor EQUAL lfactor'''
    p[0]=('==',p[1],p[3])

def p_lexpr_eq_string(p):
    '''lexpr : STRING EQUAL STRING'''
    p[0] = ('==', p[1], p[3])

def p_lexpr_not_eq(p):
    '''lexpr : factor NOT_EQUAL factor'''
    p[0]=('<>',p[1],p[3])

def p_plexpr_not_eq_factor(p):
    '''lexpr : lfactor NOT_EQUAL lfactor'''
    p[0]=('<>',p[1],p[3])

def p_lexpr_not_eq_string(p):
    '''lexpr : STRING NOT_EQUAL STRING'''
    p[0] = ('<>', p[1], p[3])

def p_lexpr_and(p):
    '''lexpr : lfactor AND lfactor
                | lfactor AND func_call_stmt
                | func_call_stmt AND func_call_stmt
                | func_call_stmt AND lfactor'''
    p[0]=('and',p[1],p[3])


def p_lexpr_or(p):
    '''lexpr : lfactor OR lfactor
                | lfactor OR func_call_stmt
                | func_call_stmt OR func_call_stmt
                | func_call_stmt OR lfactor'''
    p[0]=('or',p[1],p[3])

def p_lexpr_xor(p):
    '''lexpr : lfactor XOR lfactor
                | lfactor XOR func_call_stmt
                | func_call_stmt XOR func_call_stmt
                | func_call_stmt XOR lfactor'''
    p[0]=('xor',p[1],p[3])

def p_lexpr_not(p):
    '''lexpr : NOT lfactor
                | NOT func_call_stmt'''
    p[0]=('not',p[2])

def p_lexpr_factor(p):
    '''lexpr : lfactor'''
    p[0]=p[1]

def p_lfactor_true(p):
    '''lfactor : TRUE'''
    p[0] = p[1]

def p_lfactor_false(p):
    '''lfactor : FALSE'''
    p[0] = p[1]

def p_lfactor_lexpr(p):
    '''lfactor : LPAR lexpr RPAR'''
    p[0] = ('()',p[2])

# def p_lfactor_func_call(p):
#     '''lfactor : func_call_stmt'''
#     p[0]=p[1]

def p_if_stmt(p):
    '''if_stmt : IF lexpr THEN stmt_block END IF %prec IFX'''
    p[0]=('if',p[1],p[4])

def p_if_stmt_else(p):
    '''if_stmt : IF lexpr THEN stmt_block ELSE stmt_block END IF'''
    p[0]=('if_else',p[1],p[4],p[6])

def p_while_stmt(p):
    '''while_stmt : WHILE lexpr DO stmt_block END WHILE'''
    p[0]=('while',p[1],p[4])


def p_stmt_block_single(p):
    '''stmt_block : stmt'''
    p[0]=p[1]

def p_stmt_block_multi(p):
    '''stmt_block : stmt_block stmt'''
    p[0]=('stmt_block',p[1],p[2])

def p_stmt(p):
    '''stmt : assign
            | if_stmt
            | while_stmt
            | func_decl_stmt
            | func_call_stmt
            | print_stmt
            | return_stmt
            | continue_stmt
            | exit_stmt'''
    p[0]=p[1]

def p_fun_decl_stmt_no_param(p):
    '''func_decl_stmt : FUNCTION ID LPAR RPAR stmt_block END FUNCTION'''
    p[0]=("function_decl",p[2],p[5])

def p_func_decl_stmt_param(p):
    '''func_decl_stmt : FUNCTION ID LPAR arg_list RPAR stmt_block END FUNCTION'''
    p[0]=("function_decl",p[2],p[4],p[6])

def p_arg_list(p):
    '''arg_list : arg_list COMMA ID'''
    p[0]=('arg_list',p[1],p[3])

def p_arg_list_single(p):
    '''arg_list : ID'''
    p[0]=p[1]

def p_func_call_stmt(p):
    '''func_call_stmt : ID LPAR RPAR'''
    p[0]=("func_call",p[1])

def p_func_call_par_stmt(p):
    '''func_call_stmt : ID LPAR param_list RPAR'''
    p[0]=("func_call",p[1],p[3])

def p_param_list_multi(p):
    '''param_list : param_list COMMA param'''
    p[0]=("param_list",p[1],p[2])

def p_param_list_single(p):
    '''param_list : param'''
    p[0] = p[1]

def p_param(p):
    '''param : expr
            | lexpr
            | STRING'''
    p[0]=p[1]

def p_print_stmt_expr(p):
    '''print_stmt : PRINT param'''
    p[0]=("print",p[1])

def p_return_stmt_empty(p):
    '''return_stmt : RETURN %prec RETURNX'''
    p[0]=("return",None)

def p_return_stmt_param(p):
    '''return_stmt : RETURN param'''
    p[0]=("return",p[2])

def p_continue_stmt(p):
    '''continue_stmt : CONTINUE WHILE'''
    p[0]=("continue")

def p_exit(p):
    '''exit_stmt : EXIT WHILE'''
    p[0]=("exit")

def p_error(p):
    if p:
        print("Syntax error at line {0}: {1} , '{2}'!".format(p.lineno,p.type,p.value))
    else:
        print("Unexpected end of data")

parser=yacc.yacc()