from math import sqrt
from typing import List


class Vector:
    def __init__(self, coor:List[float]):
        self.coor = list(coor)
    
    def check_len(self, v2: 'Vector'):
        if (len(self.coor) != len(v2.coor)):
            raise ValueError()
        
    def __repr__(self):
        return f"Vector({self.coor})"
        
    def __eq__(self, v2: 'Vector'):
        return self.coor == v2.coor

    def __add__(self, v2: 'Vector') -> 'Vector':
        self.check_len(v2)
        return Vector([a + b for a, b in zip(self.coor, v2.coor)])

    def __sub__(self, v2:'Vector') -> 'Vector':
        self.check_len(v2)
        return Vector([a - b for a, b in zip(self.coor, v2.coor)])

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector([a * scalar for a in self.coor])

    def __rmul__(self, scalar:float) -> 'Vector':
        return self.__mul__(scalar)
    
    def __len__(self):
        return (len(self.coor))
    
    def __getitem__(self, i):
        return self.coor[i]

    def dot(self, v2: 'Vector') -> float:
        self.check_len(v2)
        return sum(a * b for a, b in zip(self.coor, v2.coor))

    @property
    def norm(self) -> float:
        return sqrt(self.dot(self))
    


