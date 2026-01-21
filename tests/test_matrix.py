import pytest
from src.matrix import Matrix
from src.vector import Vector

def test_init_validity():
    with pytest.raises(ValueError):
        Matrix([])
    with pytest.raises(ValueError):
        Matrix([[1, 2], [1]])

def test_shape():
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    assert m.shape == (2, 3)

def test_getitem_vector():
    v = Vector([10, 20])
    assert v[0] == 10
    assert v[1] == 20

def test_matmul_identity():
    I = Matrix([[1, 0], [0, 1]])
    v = Vector([5, 10])
    assert (I @ v) == Vector([5, 10])

def test_matmul_rotation_90():
    # [ 0 -1 ] [ x ] = [ -y ]
    # [ 1  0 ] [ y ]   [  x ]
    R = Matrix([[0, -1], [1, 0]])
    v = Vector([1, 0])
    assert (R @ v) == Vector([0, 1])

def test_matmul_dimension_mismatch():
    A = Matrix([[1, 2], [3, 4]]) # 2x2
    v = Vector([1, 2, 3])        # 3x1
    with pytest.raises(ValueError):
        A @ v # type: ignore

def test_matrix_matrix_multiplication():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = A @ B
    assert C[0] == pytest.approx([19, 22])
    assert C[1] == pytest.approx([43, 50])

def test_solve_with_pivoting_zero_pivot_case():
    # Requires a row swap to avoid zero pivot
    A = Matrix([[0, 1], [1, 1]])
    b = Vector([1, 2])
    x = A.solve(b)
    assert x.coords == pytest.approx([1.0, 1.0])

def test_determinant_value_and_sign():
    # Basic determinant
    B = Matrix([[1, 2], [3, 4]])
    assert B.det == pytest.approx(-2.0)

    # Permutation matrix with one swap -> det = -1
    P = Matrix([[0, 1], [1, 0]])
    assert P.det == pytest.approx(-1.0)

def test_determinant_raises_on_singular():
    # Singular matrix (rows are linearly dependent)
    S = Matrix([[1, 2], [2, 4]])
    with pytest.raises(ValueError):
        _ = S.det

def test_transpose_rectangular():
    A = Matrix([[1, 2, 3], [4, 5, 6]])  # 2x3
    AT = A.transpose                    # 3x2
    assert AT.shape == (3, 2)
    assert AT[0].coords == [1, 4]
    assert AT[1].coords == [2, 5]
    assert AT[2].coords == [3, 6]

def test_plu_decomposition():
    A = Matrix([[4, 3], [6, 3]])
    P, L, U = A.plu_decomposition()

    reconstructed = L @ U
    expected = P @ A
    assert reconstructed == expected

def test_inverse():
    A = Matrix([[1, 2], [3, 4]])
    A_inv = A.inverse
    I = A @ A_inv
    assert I[0][0] == pytest.approx(1.0)
    assert I[0][1] == pytest.approx(0.0)
    
    assert I[1][0] == pytest.approx(0.0)
    assert I[1][1] == pytest.approx(1.0)

def test_rref():
    A = Matrix([[2, 4], [1, 3]])
    R = A.rref()
    assert R[0].coords == pytest.approx([1, 0])
    assert R[1].coords == pytest.approx([0, 1])