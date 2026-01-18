# Linear Algebra from Scratch

Minimal, pure-Python implementations of core Linear Algebra primitives (`Vector` and `Matrix`). Built from scratch to verify concepts inspired by Gilbert Strang's _Introduction to Linear Algebra_ (MIT 18.06). The focus is mathematical clarity over performance.

## Features

- **Vectors:** Addition, subtraction, scalar multiplication, division, dot product, Euclidean norm.
- **Matrices:** Addition, subtraction, scalar multiplication, matrix–vector (`A @ x`) and matrix–matrix (`A @ B`) multiplication.
- **Solving `Ax = b`:** Gaussian elimination with partial pivoting, followed by back substitution.
- **Determinant:** Computed from the upper-triangular form; sign corrected by row-swap count.
- **Safety:** Dimension checks and informative errors for mismatches and singular systems.

## Installation

No external dependencies. Use directly in any Python 3.9+ environment.

## Quick Start

```python
from src import Matrix, Vector

# Define a 2x2 matrix and a vector
A = Matrix([[2, 0], [0, 3]])
x = Vector([1, 10])

# Matrix–vector multiplication
b = A @ x
print(b)          # Prints the coordinate list: [2, 30]
print(b.norm)     # 30.066592756745816

# Matrix arithmetic
M1 = Matrix([[1, 2], [3, 4]])
M2 = Matrix([[5, 6], [7, 8]])
M3 = M1 + M2      # [[6, 8], [10, 12]]
M4 = M1 - M2      # [[-4, -4], [-4, -4]]
M5 = 2 * M1       # [[2, 4], [6, 8]]
M6 = M1 @ M2      # [[19, 22], [43, 50]]

# Solve Ax = b
A = Matrix([[2, 1], [3, 4]])
b = Vector([5, 15])
x = A.solve(b)
print(x.coords)   # [1.0, 3.0]

# Determinant
B = Matrix([[1, 2], [3, 4]])
print(B.det)      # -2.0
```

## API Reference

### Vector (src/vector.py)

- **`Vector(coords: List[float])`**: Construct from a list of numbers.
- **`coords: List[float]`**: Property returning the coordinate list.
- **`__len__()`**: Vector dimension.
- **`__getitem__(i)` / `__setitem__(i, value)`**: Index access.
- **`__add__(v)` / `__sub__(v)`**: Element-wise operations (dimension-checked).
- **`__mul__(scalar)` / `__rmul__(scalar)`**: Scalar multiplication.
- **`__truediv__(scalar)`**: Scalar division (error on zero).
- **`dot(v)`**: Dot product (dimension-checked).
- **`norm`**: Euclidean norm $\|v\|_2$.
- **`__repr__()`**: Prints the coordinate list (e.g., `[1, 2]`).

### Matrix (src/matrix.py)

- **`Matrix(rows: List[List[float]])`**: Construct from row lists; all rows must have equal length.
- **`rows`**: List of `Vector` rows.
- **`shape`**: Tuple `(m, n)` for `m` rows and `n` columns.
- **`row(i)` / `col(j)`**: Accessors returning a `Vector`.
- **`__getitem__(i)` / `__setitem__(i, Vector)`**: Row access and mutation.
- **Arithmetic**: `+`, `-`, `scalar * M`, `M * scalar`.
- **Multiplication**: `A @ x` (matrix–vector) and `A @ B` (matrix–matrix).
- **`swap_rows(i, j, b: Optional[Vector] = None)`**: Swap two rows; also swaps entries of `b` if provided.
- **`gaussian_elimination(b: Optional[Vector] = None) -> int`**: In-place elimination with partial pivoting. Returns the count of row swaps (used by `det`). If `b` is provided, it is updated in-place to maintain the augmented system.
- **`back_substitution(b: Vector) -> Vector`**: Solve the upper-triangular system using back substitution.
- **`solve(b: Vector) -> Vector`**: Convenience method; runs elimination + back substitution and returns `x`.
- **`copy() -> Matrix`**: Deep copy of the matrix rows.
- **`det`**: Determinant for square matrices. Creates a copy, runs elimination, multiplies diagonal, and applies `$(-1)^{\text{swap\_count}}$` for row swaps.

## Design Notes

- **Partial Pivoting**: `gaussian_elimination()` selects the largest absolute pivot in each column and swaps rows when needed to avoid zero/unstable pivots.
- **In-Place Semantics**: Elimination modifies the matrix (and `b`, if provided) in-place. The method returns the swap count for determinant calculation; callers like `solve()` ignore the count.
- **Numerical Tolerance**: A pivot is treated as zero if its absolute value is `< 1e-10` (configurable in code if desired).

## Limitations

- **Square Matrices**: `det` and `solve` are intended for square systems.
- **Bounds**: `row(i)` / `col(j)` rely on Python indexing; out-of-range indices raise `IndexError`.
- **Type Assumptions**: Elements are numeric (int/float); no complex number support.

## Development & Testing

Run the playground demo:

```bash
python playground.py
```

Unit tests are provided under `tests/`. If `pytest` is available:

```bash
pytest -q
```

## Roadmap

- LU factorization and forward/backward substitution.
- Support for matrix inverses and rank.
- Optional tolerance configuration and improved numerical stability controls.
- More test coverage: matrix–matrix multiplication, solve edge cases, singular detection.
