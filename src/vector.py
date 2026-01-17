from math import sqrt
from typing import List


class Vector:
    def __init__(self, coor:List[float]):
        self.coor = list(coor)
    
    def check_len(self, v2: 'Vector'):
        """
        Verifies that the argument has the same dimension as self

        Args:
            v2 (Vector): The vector to compare self to.

        Raises:
            ValueError: If dimensions do not match
        """
        if (len(self.coor) != len(v2.coor)):
            raise ValueError()
        
    def __repr__(self):
        """
        toString function to print the vector in the right format.

        Returns: A string representing the vector coordinates.
        """
        return f"Vector({self.coor})"
        
    def __eq__(self, v2: 'Vector'):
        """
        Checks if two vectors are element-wise equal.
        Args: 
            v2 (Vector): The vector from which we want to compare coordinates with self's coordinates.
        """
        return self.coor == v2.coor

    def __add__(self, v2: 'Vector') -> 'Vector':
        """ 
        Computes the element-wise sum of two vectors.

        Args:
            v2 (Vector): The vector to add. Must have same dimensions.
        Raises:
            ValueError: If dimensions are not the sames.
        """
        self.check_len(v2)
        return Vector([a + b for a, b in zip(self.coor, v2.coor)])

    def __sub__(self, v2:'Vector') -> 'Vector':
        """
        Computes the element-wise subtraction of two vectors.

        Args:
            v2 (Vector): The vector to subtract. Must have same dimensions.
        Raises:
            ValueError: If dimensions are not the same.
        """
        self.check_len(v2)
        return Vector([a - b for a, b in zip(self.coor, v2.coor)])

    def __mul__(self, scalar: float) -> 'Vector':
        """
        Computes the element-wise multiplication of a scalar and a vector.

        Args:
            scalar (float)
        """
        return Vector([a * scalar for a in self.coor])

    def __rmul__(self, scalar:float) -> 'Vector':
        """
        Computes the reverse multiplication of a vector and a scalar.

        Args:
            scalar (float)
        """
        return self.__mul__(scalar)
    
    def __len__(self):
        """
        Returns the length of the Vector coordinates.
        """
        return (len(self.coor))
    
    def __getitem__(self, i):
        """
        Returns item i of the coordinates of the Vector.
        """
        return self.coor[i]

    def dot(self, v2: 'Vector') -> float:
        """
        Computes the dot product of two vectors.

        Args:
            v2 (Vector): The vector with which the dot product is performed.
        Raises:
            ValueError: If dimensions are not the same.
        """
        self.check_len(v2)
        return sum(a * b for a, b in zip(self.coor, v2.coor))

    @property
    def norm(self) -> float:
        """
        Returns the norm of a vector (square root of the dot product of the vector and itself).
        """
        return sqrt(self.dot(self))
    


