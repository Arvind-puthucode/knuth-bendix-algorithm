""" this is where superposition of sub rules to take place """
from unification import UnificationResult,unify,unify_terms,print_unify
from typing import Union
from term import Term
from variable import Variable
class KnuthBendix:
    def __init__(self):
        self.rules = []  # List to store the rules in the form lhs -> rhs

    def add_rule(self,rule):
        """
        Add a rule to the list of rules.
        """
        self.rules.append(rule)

    def superposition(self,term1:Union[Term,Variable],term2:Union[Term,Variable]):
        t1_els=term1.elements()
        t1_els.add(term1)
        t1_els=list(t1_els)
        t2_els=term2.elements()
        t2_els.add(term2)
        t2_els=list(t2_els)
        for i in range(len(t1_els)):
            for j in range(len(t2_els)):
                unification,t1_d,t2_d=unify_terms(t1_els[i],t2_els[j])
                """ these terms should be unified in the terms t1,t2 
                and t1_dict and t2_dict should be used so as to check if critical pair formed"""
                #print(f'result of unification:{unification}')
                if(unification.unifiable):
                    print(f"unifier sub term for terms :{t1_els[i]} and {t2_els[j]}:{unification}")
                    # sub term unified must be edited back in the original term 
                else:
                    print(f"unification not possible for sub term for terms {t1_els[i]} and {t2_els[j]}:{unification}")
                    
        
        pass       
    
    def knuthbendix(self):
        """
        Apply the superposition rule to generate new rules.
        """
        new_rules = []
        for i, [lhs1, rhs1] in enumerate(self.rules):
            for j, [lhs2, rhs2] in enumerate(self.rules):
                print(f"\n------------------\nfor rule:{i}:{j}")
                print(f"\n{lhs1}->{lhs2}\n")
                self.superposition(lhs1,lhs2)
                print("\n-------------------\n ")
                # adde new rules to the existing rules
    

# Usage example
kb = KnuthBendix()
zero=Variable("0")
x=Variable("x1")
x2=Variable("x2")
x3=Variable("x3")
minusx3=Term("-",x3)
rule1=[Term("+",zero,x),x]
rule2=[Term("+",x2,zero),x2]
rule3=[Term("+",x3,minusx3),0]
x4=Variable("x4")
y4=Variable("y4")
z4=Variable("z4")
rule4=[Term("+",Term("+",x4,y4),z4),Term("+",x4,Term("+",y4,z4))]
rules=[rule1,rule2,rule3,rule4]
for r in rules:
    kb.add_rule(r)

kb.knuthbendix()

# You would implement your term unification and substitution application logic
# in the `unify_terms` and `apply_substitution` methods.
