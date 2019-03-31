import sys

def read_in(path='../memory_cycle_assigner/front_end_output'):
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
    
def read_glossary(path='../memory_cycle_assigner/front_end_output'):
    glossary = None
    with open(path, 'r') as f:
        content = f.read()
        glossary = content.split('---')[1]
    return glossary
    
if __name__ == '__main__':
    read_in()