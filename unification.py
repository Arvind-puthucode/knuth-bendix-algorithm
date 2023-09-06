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
            s+=f'\n{i}:{self.unifier[i]}'
        return f'{self.unifiable}:{s}'
    def print_unifier(self):
        for i in self.unifier.keys():
            s+=f'{i}:{self.unifier[i]}'
        print(f'{self.unifiable}:{s}')
def unify_terms(t1: Union[Term,Variable], t2: Union[Term,Variable]):
    t1_dict={}
    t2_dict={}
    unification_term=unify(t1,t2,t1_unification_dict=t1_dict,t2_unification_dict=t2_dict)
    
    return [unification_term,t1_dict,t2_dict]

def unify(t1: Union[Term,Variable], t2: Union[Term,Variable],t1_unification_dict={},t2_unification_dict={}) -> UnificationResult:
    if(t1 in t1_unification_dict and t1_unification_dict[t1]!=t2):
        return UnificationResult(False,{})
    if(t2 in t2_unification_dict and t2_unification_dict[t2]!=t1):
        return UnificationResult(False,{})
        
    if isinstance(t1,Variable):
        if(isinstance(t2,Variable)):
            t1_unification_dict[t1]=t2
            t2_unification_dict[t2]=t1
            return UnificationResult(True,{t1:t2})
        
        else:
            # if t1 in t2 where t2 is a term then there is an issue
            if(t1 in t2.elements()):
                return UnificationResult(False,{})
            else:
                # t1 can be subsituted by t2 then 
                t1_unification_dict[t1]=t2
                t2_unification_dict[t2]=t1
                return UnificationResult(True,{t1:t2})
    
    elif isinstance(t2,Variable):
        if(isinstance(t1,Variable)):
            
            t1_unification_dict[t1]=t2
            t2_unification_dict[t2]=t1
            return UnificationResult(True,{t1:t2})
        
        else:
            # if t2 in 12 where t1 is a term then there is an issue
            if(t2 in t1.elements()):
                return UnificationResult(False,{})
            else:
                # t1 can be subsituted by t2 then
                t1_unification_dict[t1]=t2
                t2_unification_dict[t2]=t1
                return UnificationResult(True,{t1:t2})
            
    elif t1.operation != t2.operation:
        return UnificationResult(False, {})

    else:
        unifier = {}
        for subterm1, subterm2 in zip(t1.subterms, t2.subterms):
            #print('stage ',subterm1,subterm2)
            subunification = unify(subterm1, subterm2,t1_unification_dict,t2_unification_dict)
            if not subunification.unifiable:
                return UnificationResult(False, {})
            #print('unifier',unifier,subunification)
            for key, value in subunification.unifier.items():
                unifier[key] = value
        return UnificationResult(True, unifier)

# Testing the unification algorithm
def print_unify(term1:Union[Term,Variable],term2:Union[Term,Variable]):
    result = unify(term1, term2)
    if result.unifiable:
        print(f"Terms:{term1} and {term2} are unifiable.\n Unifier:", result)
    else:
        print(f"Terms:{term1} and {term2} are not unifiable.")
def main():
    # Creating variables
    a = Variable("a")
    x = Variable("x")
    y = Variable("y")
    z=Variable("z")
    X=Variable("X")
    Y=Variable("Y")
    Z=Variable("Z")
    # Constructing terms
    """ the first example checked here is -a+a and x+y to be unified
    the second example is (x+y)+z and x+(y+z) and the third example is 
    (x+y)+(x-y) and x+x this is not unfiable 
    """
    term11 = Term("+", Term("-", a), a)
    term12 = Term("+", x,y)
    print_unify(term11,term12)

    termxy=Term("+",x,y)
    termxy_z=Term("+",termxy,z)
    termYZ=Term("+",Y,Z)
    termx_yz=Term("+",X,termYZ)
    print_unify(termx_yz,termxy_z)

    termxmy=Term("-",x,y)
    term31=Term("+",termxmy,termxy)
    term32=Term("+",X,X)
    print_unify(term31,term32)

    zero=Variable("0")
    x0=Variable("x0")
    x1=Variable("x1")
    """x+0 and 0+x"""
    term41=Term("+",x0,zero)
    term42=Term("+",zero,x1)
    print_unify(term41,term42)
main()