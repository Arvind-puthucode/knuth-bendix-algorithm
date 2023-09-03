from typing import Tuple, List, Dict
from term import Term
from typing import Union

from variable import Variable
class UnificationResult:
    def __init__(self, unifiable: bool, unifier: Dict[Variable, Term]):
        self.unifiable = unifiable
        self.unifier = unifier
    def __str__(self) -> str:
        s=''
       # print(self.unifier,'unifier')
        for i in self.unifier.keys():
            s+=f'{i}:{self.unifier[i]}'
        return f'{self.unifiable}:{s}'
    def print_unifier(self):
        for i in self.unifier.keys():
            s+=f'{i}:{self.unifier[i]}'
        print(f'{self.unifiable}:{s}')
unfication_dict={}
def unify(t1: Union[Term,Variable], t2: Union[Term,Variable]) -> UnificationResult:
    if isinstance(t1,Variable):
        if(isinstance(t2,Variable)):
            unfication_dict[t1]=t2
            return UnificationResult(True,{t1:t2})
        
        else:
            # if t1 in t2 where t2 is a term then there is an issue
            if(t1 in t2.elements()):
                return UnificationResult(False,{})
            else:
                # t1 can be subsituted by t2 then
                unfication_dict[t1]=t2
                return UnificationResult(True,{t1,t2})
    
    elif isinstance(t2,Variable):
        if(isinstance(t1,Variable)):
            unfication_dict[t2]=t1
            return UnificationResult(True,{t2:t1})
        
        else:
            # if t2 in 12 where t1 is a term then there is an issue
            if(t2 in t1.elements()):
                return UnificationResult(False,{})
            else:
                # t1 can be subsituted by t2 then
                unfication_dict[t2]=t1
                return UnificationResult(True,{t2:t1})
            
    elif t1.operation != t2.operation:
        return UnificationResult(False, {})

    else:
        unifier = {}
        for subterm1, subterm2 in zip(t1.subterms, t2.subterms):
            print('stage ',subterm1,subterm2)
            subunification = unify(subterm1, subterm2)
            if not subunification.unifiable:
                return UnificationResult(False, {})
            print('unifier',unifier,subunification)
            for key, value in subunification.unifier.items():
                unifier[key] = value
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
