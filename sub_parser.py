import sys
import os
import ast

def read_in(path='front_end_output'):
    clauses = []
    with open(path, 'r') as f:
        content = f.readlines()
        for line in content:
            if line[0] == '0': break # this is the end of the clauses
            clauseCNF = line[:-1].split(' ')
            clauseCNF = list(filter(None, clauseCNF))
            clauseCNF = list(map(lambda x: int(x), clauseCNF))
            clauses.append(clauseCNF)
    return clauses

def read_glossary(path='front_end_output'):
    glossary = {1:1}
    try:
        with open(path, 'r') as f:
            try:
                content = f.read()
                dic = content.split('---')
                glossary = ast.literal_eval(dic[1])
            except:
                print('Content could not be translated to pure dictionary, contrary to expectation.')
    except: 
        print('Error reading the output file. Maybe the previous program (DPLL) broke somewhere.')
    return glossary

if __name__ == '__main__':
    read_in()