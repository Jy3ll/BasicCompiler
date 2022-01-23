import BasicLexer
import BasicParser
import sys

sys.setrecursionlimit(10000)

level=0

def Compile(ast_node):
    global level
    if isinstance(ast_node,tuple):
        if ast_node[0]=='stmt_block':
            return Compile(ast_node[1])+Compile(ast_node[2])
        elif ast_node[0]=='func_decl':
            if len(ast_node)==3: #argless
                level+=1
                result= (level-1)*'\t'+'def '+Compile(ast_node[1])+'():\n'+Compile(ast_node[2])
                level-=1
                return result
            else: #with arglist
                level += 1
                result = (level - 1) * '\t' + 'def ' + Compile(ast_node[1]) + '('+Compile(ast_node[2])+'):\n' + Compile(ast_node[3])
                level -= 1
                return result

        elif ast_node[0]=='func_call':
            if len(ast_node)==2: #argless
                return (level*'\t')+Compile(ast_node[1])+'()'
            else: #with paramlist
                return (level * '\t') + Compile(ast_node[1]) + '('+Compile(ast_node[2])+')'
        elif ast_node[0]=='arg_list':
            return Compile(ast_node[1])+','+Compile(ast_node[2])
        elif ast_node[0]=='param_list':
            return Compile(ast_node[1])+','+Compile(ast_node[2])
        elif ast_node[0]=='return':
            if ast_node[1] is None:
                return (level*'\t')+'return\n'
            else:
                return (level*'\t')+'return '+Compile(ast_node[1])+'\n'
        elif ast_node[0]=='print':
            return (level*'\t')+'print('+Compile(ast_node[1])+')\n'
        elif ast_node[0]=='while':
            level+=1
            result=((level-1)*'\t')+'while '+Compile(ast_node[1])+':\n'+Compile(ast_node[2])
            level-=1
            return result
        elif ast_node[0]=='if':
            level+=1
            result=""
            if len(ast_node)==3: #if
                result=((level-1)*'\t')+'if '+Compile(ast_node[1])+':\n'+ Compile(ast_node[2])
            else: #if_else
                result=((level-1)*'\t')+'if '+Compile(ast_node[1])+':\n'+ Compile(ast_node[2])+\
                       ((level-1)*'\t')+'else:\n'+Compile(ast_node[3])
            level-=1
            return result
        elif ast_node[0]=='()':
            return '('+Compile(ast_node[1])+')'
        elif ast_node[0]=='not':
            return 'not '+Compile(ast_node[1])
        elif ast_node[0]=='xor':
            return Compile(ast_node[1])+'!='+Compile(ast_node[2])
        elif ast_node[0]=='or':
            return Compile(ast_node[1])+' or '+Compile(ast_node[2])
        elif ast_node[0]=='and':
            return Compile(ast_node[1])+' and '+Compile(ast_node[2])
        elif ast_node[0]=='==':
            return Compile(ast_node[1])+'=='+Compile(ast_node[2])
        elif ast_node[0]=='<>':
            return Compile(ast_node[1])+'!='+Compile(ast_node[2])
        elif ast_node[0]=='<=':
            return Compile(ast_node[1])+'<='+Compile(ast_node[2])
        elif ast_node[0]=='>=':
            return Compile(ast_node[1])+'>='+Compile(ast_node[2])
        elif ast_node[0]=='<':
            return Compile(ast_node[1])+'<'+Compile(ast_node[2])
        elif ast_node[0]=='>':
            return Compile(ast_node[1])+'>'+Compile(ast_node[2])
        elif ast_node[0]=='=':
            return (level*'\t')+Compile(ast_node[1])+'='+Compile(ast_node[2])+'\n'
        elif ast_node[0]=='uminus':
            return '-'+Compile(ast_node[1])
        elif ast_node[0]=='+':
            return Compile(ast_node[1])+'+'+Compile(ast_node[2])
        elif ast_node[0]=='-':
            return Compile(ast_node[1])+'-'+Compile(ast_node[2])
        elif ast_node[0]=='*':
            return Compile(ast_node[1])+'*'+Compile(ast_node[2])
        elif ast_node[0]=='/':
            return Compile(ast_node[1])+'/'+Compile(ast_node[2])
        elif ast_node[0]=='mod':
            return Compile(ast_node[1])+'%'+Compile(ast_node[2])

    else:
        if str(ast_node)=='continue':
            return (level*'\t')+'continue\n'
        elif str(ast_node)=='exit':
            return (level*'\t')+'break\n'
        else:
            return str(ast_node)


class Compiler:
    def __init__(self):
        pass
    def compile(self,filename):
        pure_name=filename[:-2]
        with open(filename,'r') as in_file:
            parser = BasicParser.parser
            text = in_file.read()
            ast = parser.parse(text, lexer=BasicLexer.lexer)
            compilation_result=Compile(ast)
            with open(pure_name+'.py','w') as out_file:
                out_file.write(compilation_result)