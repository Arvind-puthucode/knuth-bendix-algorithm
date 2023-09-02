from variable import  Variable
from typing import Union
class Term:
    def __init__(self, operation=None, *subterms):
        """a term can be 
            1) variable
            2) subterm
            3) subterm+variable
            4) subterm+subterm"""
        self.operation = operation
        self.subterms = subterms
        self.name=None
    @classmethod
    def init_from_name(cls, name):
        instance = cls()  # Create an instance of the class
        instance.name = name  # Set the name attribute
        return instance
    def is_variable(self,v=None):
        if isinstance(v,Variable):
            return True
        return False
    def complexity(self):
        if self.is_variable(self):
            return 0  # Variables have complexity 0
        elif self.operation:
            return self.leftmost_subtree_length(self)  # Measure complexity based on leftmost subtree

    def leftmost_subtree_length(self,term)->int:
        #print('term',term,type(term),term.subterms)
        if self.is_variable(term):
           # print('variable',term)
            return 0
        elif term.operation:
            left_subtree_length = self.leftmost_subtree_length(term.subterms[0]) if len(list(term.subterms))>0 else 0
           # print('tree_lenght',term,left_subtree_length+1)
            return max(left_subtree_length,0)+1
        return 0
    def __str__(self):
        if self.name:
            return self.name
        elif self.operation:
            subterm_strings=[]
            for subterm in self.subterms:
                if(subterm!=None):
                   # print('subterm',subterm)
                    subterm_strings.append(str(subterm))
            self.name=f"T{self.operation}({', '.join(subterm_strings)})"
            return self.name
        return ""
class Operation:
    def __init__(self, operator, operands:list[Union[Term, Variable]]):
        self.operator = operator
        self.operands = operands
    def result(self,)->Term:
        """
        the operation i have initially implemented for string but later on the operation has to be appropriated
        """
        return Term(self.operator,*self.operands)
    def __str__(self) -> str:
        print(f'Operator Class: operator:{self.operator},operands:{self.operands}')

def compare_complexity(exp1:Term,exp2:Term):
    # Compare complexity
    complexity_expression1 = exp1.complexity()
    complexity_expression2 = exp2.complexity()

    print("Complexity of expression 1:", complexity_expression1)
    print("Complexity of expression 2:", complexity_expression2)

    if complexity_expression1 < complexity_expression2:
        print("Expression 1 is simpler.")
    else:
        print("Expression 2 is simpler.")

def main():

    # Creating variables
    a = Variable("a")

    # Constructing the expression: -a + a
    eg1_subterm1=Operation("-", [a]).result()
    expression = Term("+",eg1_subterm1 , a)

    print(expression)  # Prints: (-a + a)
    # for better parsing logic T+(T-(Va), Va)

    # expression 2 (--a+-a)+a
    eg2_subterm11=Operation("-",[eg1_subterm1]).result()
    eg2_subterm1=Operation("+",[eg2_subterm11,eg1_subterm1]).result()
    eg2_term=Term("+",eg2_subterm1,a)
    print(eg2_term)
    # T+(T+(T-(T-(Va)),T-(Va)), Va)

    x=Variable("x")
    y=Variable("y")
    z=Variable("z")

    # expression 3  (x+y)+z
    eg3_subterm1=Operation("+",[x,y]).result()
    eg3_term=Term("+",eg3_subterm1,z)
    print('expression 3',eg3_term)

    # expression 4 x+(y+z)
    eg4_subterm2=Operation("+",[y,z]).result()
    eg4_term=Term("+",x,eg4_subterm2)
    print('expression 4',eg4_term)

    compare_complexity(eg3_term,eg4_term)
main()