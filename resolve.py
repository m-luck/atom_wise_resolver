from sub_davis_putnam_solver import *

clauses = p.read_in()
decisions = {}
lits = enumerate_literals(clauses)
res = DPLLmod(clauses, decisions, lits)
res = dict(sorted(res.items()))
resString = []
for clause in res:
    boolStr = 'T' if res[clause] == True else 'F'
    clauseStr = str(clause) + ' ' + boolStr
    resString.append(clauseStr)
resString.append('0')

output = ''
for string in resString:
    output += string + '\n'
output += '---' + p.read_glossary() + '\n---\n' + str(res)

with open('decisions','w+') as f:
    f.write(str(output))