import sub_parser as p
from typing import Dict, List, Tuple

db=True

def propagate_decision(new_decision: tuple, current_clause_list: List, current_decisions: Dict):
    '''
    Propagate decision throughout all remaining clauses.
    Returns three values of unsatisfiability, updated clauses, and updated decisions.
    '''
    target_atom = new_decision[0]
    target_truth = new_decision[1]
    updated_clauses = current_clause_list.copy()
    any_empty_clause = False
    updated_decisions = current_decisions.copy()
    updated_decisions[target_atom] = target_truth
    for i, clause in enumerate(current_clause_list):
        for lit in clause:
            updated_clause = clause.copy()
            if abs(lit) == target_atom:
                if lit < 0: 
                    if target_truth == True: 
                        updated_clause.remove(lit)
                        updated_clauses.insert(i, updated_clause)
                        updated_clauses.remove(clause)
                        if len(clause)==0: any_empty_clause = True
                    else: 
                        updated_clauses.remove(clause)
                        break
                else: 
                    if target_truth == False:
                        updated_clause.remove(lit)
                        updated_clauses.insert(i, updated_clause)
                        updated_clauses.remove(clause)
                        if len(clause)==0: any_empty_clause = True
                    else: 
                        updated_clauses.remove(clause)
                        break
    return any_empty_clause, updated_clauses, updated_decisions

def singleton_propagation(current_clause_list: List, current_decisions: Dict):
    '''
    ucl is Updated Clause List
    ud is Updated Decision List
    uns is Unsatisfiability

    If there are any clauses with only one atom, satisfy that clause.
    Returns ucl, ud, and if it results in uns.
    '''
    ucl = current_clause_list.copy()
    ud = current_decisions.copy()
    uns = False
    for clause in current_clause_list:
        if len(clause) == 1:
            singleton = clause[0]
            if singleton < 0:
                decision = (abs(singleton), False)
            else:
                decision = (abs(singleton), True)
            ud[decision[0]] = decision[1]
            uns, ucl, ud = propagate_decision(decision, ucl, ud)
            if uns: break
    return uns, ucl, ud

def pure_literal_propagation(current_clause_list: List, current_decisions: Dict):
    '''
    If a literal appears and no negation of that literal appears anywhere within all the clauses,
    satisfy that literal.
    '''
    ucl = current_clause_list.copy()
    ud = current_decisions.copy()
    uns = False
    lit_cnt = {}
    for clause in current_clause_list:
        for lit in clause:
            lit_cnt[lit] = lit_cnt.get(lit, 0) + 1 # Add to dictionary if exists.
    for lit in lit_cnt:
        if -lit not in lit_cnt: # If the negation does not exist in the clauses..
            decision = (abs(lit), False) if lit < 0 else (abs(lit), True)
            ud[decision[0]] = decision[1]
            uns, ucl, ud = propagate_decision(decision, ucl, ud)
            if uns: break
    return uns, ucl, ud
    
def check_succ(clauses: List):
    '''
    '''
    if len(clauses) == 0: return True
    else: return False

def check_f(clauses: List):
    '''
    '''
    for clause in clauses:
        if len(clause) == 0: return True
    return False

def enumerate_literals(clauses: List):
    lits = {}
    for clause in clauses:
        for lit in clause:
            lits[lit] = True
    return lits

def DPLLmod(clauses: List, decisions: Dict, lits: Dict):
    if check_succ(clauses): return decisions
    if check_f(clauses): return None
    uns, ucl, ud = singleton_propagation(clauses, decisions)
    uns, ucl, ud = pure_literal_propagation(ucl, ud)
    
    uclBackTrack, udBackTrack = ucl.copy(), ud.copy()
    for lit in lits:
        if abs(lit) not in ud:
            new_decision = (abs(lit), True)
            uns, ucl, ud = propagate_decision(new_decision, ucl, ud)
            res = DPLLmod(ucl, ud, lits)
            if res != None:
                return res 
            else:
                new_decision = (abs(lit), False)
                uns, ucl, ud = propagate_decision(new_decision, uclBackTrack, udBackTrack)
                res = DPLLmod(ucl, ud, lits)
                if res != None:
                    return res
    return None


               
    
    
    
