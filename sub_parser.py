import sys

def read_in(path='../memory_cycle_assigner/front_end_output'):
    with open(path, 'r') as f:
        content = f.readlines()
        for line in content:
            if line[0] == '0': break # this is the end of the clauses
            clauseCNF = line[:-1].split(' ')
            clauseCNF = list(map(lambda x: int(x), clauseCNF))
            print(clauseCNF)

if __name__ == '__main__':
    read_in()