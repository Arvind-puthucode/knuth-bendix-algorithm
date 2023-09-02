from typing import Tuple, List, Dict
from term import Term
from variable import Variable
class UnificationResult:
    def __init__(self, unifiable: bool, unifier: Dict[Variable, Term]):
        self.unifiable = unifiable
        self.unifier = unifier

def unify(t1: Term, t2: Term) -> UnificationResult:
    if t1.is_variable():
        if t1 == t2:
            return UnificationResult(True, {})
        elif t1 in t2.complexity():
            return UnificationResult(False, {})
        else:
            return UnificationResult(True, {t1: t2})

    elif t2.is_variable():
        if t2.name in t1.complexity():
            return UnificationResult(False, {})
        else:
            return UnificationResult(True, {t2: t1})

    elif t1.operation != t2.operation:
        return UnificationResult(False, {})

    else:
        unifier = {}
        for subterm1, subterm2 in zip(t1.subterms, t2.subterms):
            subunification = unify(subterm1, subterm2)
            if not subunification.unifiable:
                return UnificationResult(False, {})
            unifier.update(subunification.unifier)
        return UnificationResult(True, unifier)

# Testing the unification algorithm

# Creating variables
a = Variable("a")
x = Variable("x")
y = Variable("y")
z=Variable("z")
# Constructing terms
term1 = Term("+", Term("-", a), a)
term2 = Term("+", x,y)

result = unify(term1, term2)
if result.unifiable:
    print("Terms are unifiable. Unifier:", result.unifier)
else:
    print("Terms are not unifiable.")
