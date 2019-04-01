from sub_davis_putnam_solver import *
import sys

if len(sys.argv) == 1: # If there's an argument take it (independent of memory_cycles)
    clauses = p.read_in()
else:
    clauses = p.read_in(sys.argv[1]) # Else we're in a pipeline from the memory_cycle frontend (and we know where the clauses should be)
decisions = {}
lits = enumerate_literals(clauses) # Keep track of literals.
res = DPLLmod(clauses, decisions, lits) # Run resolution!
resString = []
if res != None: # If there is an answer..
    res = dict(sorted(res.items()))
    for clause in res: # Convert it to ATOM T|F format
        boolStr = 'T' if res[clause] == True else 'F'
        clauseStr = str(clause) + ' ' + boolStr
        resString.append(clauseStr)
resString.append('0')

output = ''
for string in resString:
    output += string + '\n'
output += '---' + str(p.read_glossary()) # Pass on the backmatter.

with open('decisions','w+') as f:
    f.write(str(output)) # File for the backend to read. 