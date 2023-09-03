class Variable:
    def __init__(self, name):
        self.name = name  
    def __str__(self) -> str:
        return f'V{self.name}'
    def __eq__(self,other):
        if(isinstance(other,Variable) and self.name==other.name):
            return True
        return False
    def __hash__(self) -> int:
        return hash(self.name)