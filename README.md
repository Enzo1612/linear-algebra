# Linear Algebra from Scratch

A minimal, pure-Python implementation of core Linear Algebra primitives, built from scratch to verify the concepts from Gilbert Strang's _Introduction to Linear Algebra_ (MIT 18.06).

**Goal:** Prioritize mathematical clarity and explicit implementation over performance.

## Features

### 1. Vector Operations (`src.vector`)

- **Arithmetic:** Addition (`+`), Subtraction (`-`), Scalar Multiplication (`*`, including `3 * v`).
- **Geometry:** Dot Product, Euclidean Norm ($L_2$).
- **Safety:** Strong dimension checks and type validation.

### 2. Matrix Operations (`src.matrix`)

- **Structure:** Row-major storage using `Vector` objects.
- **Access:** `row(i)` and computed `col(j)` accessors.
- **Arithmetic:** Addition (`+`), Subtraction (`-`), Scalar Multiplication (`*`, including `3 * M`).
- **Multiplication ($Ax$):** Implements Matrix-Vector multiplication using the **Row Picture** (Dot product of each row with vector $x$).
- **Multiplication ($AB$):** Implements Matrix-Matrix multiplication.

## Usage

The library exposes a clean API via `src`:

```python
from src import Matrix, Vector

# 1. Define a 2x2 Matrix (e.g., a scaling matrix)
A = Matrix([
    [2, 0],
    [0, 3]
])

# 2. Define a Vector
x = Vector([1, 10])

# 3. Compute b = Ax
b = A @ x
print(b)
# Output: Vector([2.0, 30.0])

# 4. Check Norm
print(b.norm)
# Output: 30.066592756745816

# 5. Matrix arithmetic
M1 = Matrix([[1, 2], [3, 4]])
M2 = Matrix([[5, 6], [7, 8]])

# Addition and subtraction
M3 = M1 + M2  # Matrix([[6, 8], [10, 12]])
M4 = M1 - M2  # Matrix([[-4, -4], [-4, -4]])

# Scalar multiplication
M5 = 2 * M1   # Matrix([[2, 4], [6, 8]])

# Matrix-Matrix multiplication
M6 = M1 @ M2  # Matrix([[19, 22], [43, 50]])
```
