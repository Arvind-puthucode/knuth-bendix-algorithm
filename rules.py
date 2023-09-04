""" this is where superposition of sub rules to take place """
from unification import UnificationResult,unify
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
        t1_set=term1.elements()
        t1_set.add(term1)
        t2_set=term2.elements()
        t2_set.add(term2)
        print('set of terms ')
        for i in t1_set:
            for j in t2_set:
                pass        
    
    def knuthbendix(self):
        """
        Apply the superposition rule to generate new rules.
        """
        new_rules = []
        for i, [lhs1, rhs1] in enumerate(self.rules):
            for j, [lhs2, rhs2] in enumerate(self.rules):
                self.superposition(lhs1,lhs2)
                # adde new rules to the existing rules
        

# Usage example
kb = KnuthBendix()
zero=Variable("0")
x=Variable("x")
minusx=Term("-",x)
rule1=[Term("+",zero,x),x]
rule2=[Term("+",x,zero),x]
rule3=[Term("+",x,minusx),0]
y=Variable("y")
z=Variable("z")
rule4=[Term("+",Term("+",x,y),z),Term("+",x,Term("+",y,z))]
rules=[rule1,rule2,rule3,rule4]
for r in rules:
    kb.add_rule(r)
kb.knuthbendix()

# You would implement your term unification and substitution application logic
# in the `unify_terms` and `apply_substitution` methods.
