# playground.py
from src import Matrix
from src import Vector

# Test data
A = Matrix([
    [1, 2],
    [3, 8]
])

print(f"Determinant: {A.det}")

A = Matrix([[2, 1], [3, 4]])
b = Vector([5, 15])
print("Solution:", A.solve(b).coords)

B = Matrix([[1, 2], [3, 4]])
print(f"Det: {B.det}") # Should be 1*4 - 2*3 = -2
print(f"B is unchanged: {B.rows[1].coords}") # Should still be [3, 4]