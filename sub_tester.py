from sub_davis_putnam_solver import *

def test_enumerate_lits(clauses):
    res = enumerate_literals(clauses)
    print(res)
    return res

def test_propagate(new, clauses, decs):
    res = propagate_decision(new, clauses, decs)
    print(res)
    return res

def test_sing(clauses, decs):
    res = singleton_propagation(clauses, decs)
    print(res)
    return res

def test_pure(clauses, decs):
    res = pure_literal_propagation(clauses, decs)
    print(res)
    return res

def test_check_succ(clauses):
    res = check_succ(clauses)
    print(res)
    return res

def test_check_f(clauses):
    res = check_f(clauses)
    print(res)
    return res

def test_dpll(clauses, decs, lits):
    res = DPLLmod(clauses, decs, lits)
    print(res)
    return res

if __name__ == "__main__":
    try:
        path = p.sys.argv[1]
    except: 
        print("Supply a valid test file.")
    else:
        clauses = p.read_in(path)

        lits = test_enumerate_lits(clauses)

        test_decs = {}
        test_propagate((1,True),clauses,test_decs)
        test_sing(clauses,test_decs)
        test_pure(clauses,test_decs)
        assert test_check_succ([])
        assert test_check_f([[]])
        test_dpll(clauses, test_decs, lits)
