import pytest
from src.matrix import Matrix
from src.vector import Vector

def test_init_validity():
    # Should fail with empty rows
    with pytest.raises(ValueError):
        Matrix([])
    # Should fail with jagged rows
    with pytest.raises(ValueError):
        Matrix([[1, 2], [1]])

def test_shape():
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    assert m.shape == (2, 3)

def test_getitem_vector():
    # Verify your Vector.__getitem__ works, as Matrix relies on it
    v = Vector([10, 20])
    assert v[0] == 10
    assert v[1] == 20

def test_matmul_identity():
    I = Matrix([[1, 0], [0, 1]])
    v = Vector([5, 10])
    assert (I @ v) == Vector([5, 10])

def test_matmul_rotation_90():
    # Rotation matrix 90 degrees counter-clockwise
    # [ 0 -1 ] [ x ] = [ -y ]
    # [ 1  0 ] [ y ]   [  x ]
    R = Matrix([[0, -1], [1, 0]])
    v = Vector([1, 0])
    assert (R @ v) == Vector([0, 1])

def test_matmul_dimension_mismatch():
    A = Matrix([[1, 2], [3, 4]]) # 2x2
    v = Vector([1, 2, 3])        # 3x1
    with pytest.raises(ValueError):
        A @ v