from typing import List
from src import Vector


class Matrix:
    def __init__(self, rows: List):
        if not rows or not rows[0]:
            raise ValueError("Matrix can't be empty")
        
        length = len(rows[0])
        for row in rows:
            if len(row) != length:
                raise ValueError("All rows must have the same length")
            
        self.rows = [Vector(row) for row in rows]
    
    @property
    def shape(self):
        """
        Returns the size of the matrix as a tuple (number of rows, number of cols).
        """
        return (len(self.rows), len(self.rows[0]))
    

    def row(self, i: int):
        """
        Returns the i^th row of the matrix.

        Args:
            i (int): The index of the row.
        """
        return self.rows[i]
    
    def col(self, j: int):
        """
        Returns the j^th column of the matrix.
        
        Args:
            j (int): The index of the column.
        """
        return Vector([row[j] for row in self.rows])
    
    def __matmul__(self, x: Vector) -> Vector:
        """
        Computes the multiplication of a Matrix and a Vector. (Row . x | For every row in the matrix).
        
        Args:
            x (Vector): The vector to Multiply the matrix by. Vector length must be the same as the matrix's number of cols.
        
        Raises:
            ValueError: If the vector length is not the same as the matrix's number of columns.
        """
        m, n = self.shape
        if n != len(x):
            raise ValueError("The vector length must be the same as the matrix's number of cols")
        res = [row.dot(x) for row in self.rows]
        return Vector(res)