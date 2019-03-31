from sub_davis_putnam_solver import *
import sys

if len(sys.argv) == 1:
    clauses = p.read_in()
else:
    clauses = p.read_in(sys.argv[1])
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
output += '---' + str(p.read_glossary())

with open('../decisions','w+') as f:
    f.write(str(output))