import pytest
from src.vector import Vector

def test_add():
    v1 = Vector([1, 2])
    v2 = Vector([3, 4])
    result = v1 + v2
    assert result == Vector([4, 6])

def test_mul():
    v = Vector([1, -2])
    assert v * 3 == Vector([3, -6])
    assert 3 * v == Vector([3, -6])

def test_div():
    v = Vector([4, 8])
    assert v / 2 == Vector([2, 4])

def test_dot():
    v = Vector([1, 2])
    w = Vector([3, 4])
    assert v.dot(w) ==  11

def test_norm():
    v = Vector([3, 4])
    assert v.norm == 5.0

def test_error_handling():
    v1 = Vector([1, 2])
    v2 = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        v1 + v2