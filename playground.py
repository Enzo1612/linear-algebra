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

C = Matrix([[1,2],[3,4]])
c = Vector([5, 13])
C.swap_rows(0, 1, c)

print(f"Matrix: {[row for row in C.rows]}\n Vector: {c}")


# This used to crash. Now it should work.
D = Matrix([[0, 1], [1, 1]])
d = Vector([1, 2])

sol = D.solve(d)
print(f"Solution: {sol.coords}") 
# Expected: [1.0, 1.0]