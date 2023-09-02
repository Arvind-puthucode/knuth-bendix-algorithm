
class Variable:
    def __init__(self, name):
        self.name = name  
    def __str__(self) -> str:
        return f'V{self.name}'
    