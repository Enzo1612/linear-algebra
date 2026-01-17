from typing import List
from src.vector import Vector


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
        return (len(self.rows), len(self.rows[0]))
    

    def row(self, i: int):
        return self.rows[i]
    
    def col(self, j: int):
        return Vector([row[j] for row in self.rows])
    
    def __matmul__(self, x: Vector) -> Vector:
        m, n = self.shape
        if n != len(x):
            raise ValueError("The vector length must be the same as the matrix's number of cols")
        res = [row.dot(x) for row in self.rows]
        return Vector(res)