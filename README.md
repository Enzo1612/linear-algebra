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

#### Constructors

- **`Vector(coords: List[float])`**: Construct a vector from a list of numbers.

#### Properties

- **`coords`**: List[float] — Returns the coordinate list.
- **`norm`**: float — Euclidean norm $\|v\|_2 = \sqrt{\sum v_i^2}$.

#### Operators & Arithmetic

- **`v1 + v2`** or **`v + scalar`**: Element-wise addition (vectors must have matching dimensions).
- **`v1 - v2`** or **`v - scalar`**: Element-wise subtraction (vectors must have matching dimensions).
- **`v * scalar`** or **`scalar * v`**: Scalar multiplication.
- **`v / scalar`**: Scalar division (raises `ValueError` if scalar is 0).

#### Accessors & Indexing

- **`v[i]`**: Get the i-th coordinate.
- **`v[i] = value`**: Set the i-th coordinate.
- **`len(v)`**: Return the vector dimension.

#### Methods

- **`dot(v2: Vector) -> float`**: Dot product (dimension-checked). Raises `ValueError` if dimensions don't match.
- **`copy() -> Vector`**: Return a deep copy of the vector.
- **`check_len(v2: Vector)`**: Verify that `v2` has the same dimension; raises `ValueError` if not.

#### Special Methods

- **`__repr__()`**: String representation (prints coordinate list, e.g., `[1, 2]`).
- **`__eq__(v2)`**: Check element-wise equality.

### Matrix (src/matrix.py)

#### Constructors

- **`Matrix(rows: List[List[float]])`**: Construct from row lists; all rows must have equal length. Raises `ValueError` if empty or rows have inconsistent lengths.

#### Properties

- **`rows`**: List[Vector] — Returns the list of row vectors.
- **`shape`**: Tuple[int, int] — Returns `(m, n)` for `m` rows and `n` columns.
- **`det`**: float — Determinant for square matrices using Gaussian elimination. Creates a copy, runs elimination, multiplies diagonal elements, and applies sign correction for row swaps. Raises `ValueError` if matrix is not square or is singular.
- **`transpose`**: Matrix — Returns the transposed matrix (rows become columns).

#### Operators & Arithmetic

- **`A + B`**, **`A + v`**, **`A + scalar`**: Element-wise addition.
  - With scalar: adds to all elements.
  - With vector: converts vector to 1×n matrix and adds element-wise.
  - With matrix: adds element-wise (dimension-checked).
- **`A - B`**, **`A - v`**, **`A - scalar`**: Element-wise subtraction (same dimension rules as addition).
- **`A * scalar`** or **`scalar * A`**: Scalar multiplication on all elements.
- **`A @ x`** (matrix–vector): Row-wise dot product with vector. Returns a Vector. Raises `ValueError` if column count ≠ vector length.
- **`A @ B`** (matrix–matrix): Classical matrix multiplication. Returns a Matrix. Raises `ValueError` if A's column count ≠ B's row count.

#### Accessors & Indexing

- **`A[i]`**: Get the i-th row as a Vector.
- **`A[i] = v`**: Set the i-th row to vector `v`.
- **`A.row(i)`**: Get the i-th row (same as `A[i]`).
- **`A.col(j)`**: Get the j-th column as a Vector.

#### Methods

- **`copy() -> Matrix`**: Return a deep copy of the matrix.
- **`check_dim(b: Matrix)`**: Verify that `b` has the same shape; raises `ValueError` if not.
- **`swap_rows(i, j, b: Optional[Vector] = None)`**: Swap rows i and j. If a vector `b` is provided (used in solving systems), swap corresponding elements in `b` as well.
- **`subtract_row(source: int, target: int, mult: float)`**: Subtract `mult * row[source]` from `row[target]` (used in elimination).
- **`gaussian_elimination(b: Optional[Vector] = None) -> int`**: In-place elimination with partial pivoting. Returns the count of row swaps (used for determinant sign correction). If `b` is provided, updates it in-place to maintain the augmented system `[A | b]`.
- **`back_substitution(b: Vector) -> Vector`**: Solve the upper-triangular system (assumes `A` is already in row-echelon form). Raises `ValueError` if a zero pivot is encountered.
- **`solve(b: Vector) -> Vector`**: Convenience method to solve `Ax = b`. Calls `gaussian_elimination(b)` followed by `back_substitution(b)`. Raises `ValueError` for singular systems.
- **`plu_decomposition() -> Tuple[Matrix, Matrix, Matrix]`**: Decompose the matrix `A` into `P @ A = L @ U` using Gaussian elimination with partial pivoting.
  - Returns `(P, L, U)` where:
    - **`P`**: Permutation matrix recording row swaps.
    - **`L`**: Lower triangular matrix with multipliers below diagonal; 1s on diagonal.
    - **`U`**: Upper triangular matrix with pivots on diagonal.
  - Raises `ValueError` if not square or singular.
  - Invariant: `P @ A == L @ U`.

#### Static Methods

- **`Matrix.identity(n: int) -> Matrix`**: Return an `n × n` identity matrix with 1s on diagonal and 0s elsewhere.

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

- Support for matrix inverses and rank.
- Optional tolerance configuration and improved numerical stability controls.
