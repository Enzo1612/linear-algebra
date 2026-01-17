from typing import List
from src.vector import Vector


class Matrix:
    """A mathematical matrix with basic operations.
    
    Supports addition, subtraction, scalar multiplication, and matrix-vector
    and matrix-matrix multiplication.
    """
    
    def __init__(self, rows: List):
        """Initialize a matrix from a list of rows.
        
        Args:
            rows (List): List of lists representing matrix rows. All rows must have the same length.
            
        Raises:
            ValueError: If matrix is empty or rows have inconsistent lengths.
        """
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
    

    def row(self, i: int) -> Vector:
        """
        Returns the i^th row of the matrix.

        Args:
            i (int): The index of the row.
        """
        return self.rows[i]
    
    def col(self, j: int) -> Vector:
        """
        Returns the j^th column of the matrix.
        
        Args:
            j (int): The index of the column.
        """
        return Vector([row[j] for row in self.rows])
    
    def __matmul__(self, x):
        """
        Computes the multiplication of a Matrix and a Vector. (row dot x | For every row in the matrix).
        
        Args:
            x (Vector): The vector to Multiply the matrix by. Vector length must be the same as the matrix's number of cols.
        
        Raises:
            ValueError: If the vector length is not the same as the matrix's number of columns.
            ValueError: If the matrix 1 columns dimensions don't match the matrix 2 rows dimensions
        """
        if isinstance(x, Vector):
            m, n = self.shape
            if n != len(x):
                raise ValueError("The vector length must be the same as the matrix's number of cols")
            res = [row.dot(x) for row in self.rows]
            return Vector(res)
        
        if isinstance(x, Matrix):
            m, n = self.shape
            if n != x.shape[0]:
                raise ValueError("The matrix 1 column dimension must match the matrix 2 row dimension")
            else:
                new_rows = []
                for row_a in self.rows:
                    current_new_row_data = []

                    for j in range(x.shape[1]):
                        current_new_row_data.append(row_a.dot(x.col(j)))
                    new_rows.append(current_new_row_data)
                return Matrix(new_rows)
        else:
            raise TypeError(f"Cannot multiply Matrix by {type(x)}")
    
    def check_dim(self, b: 'Matrix'):
        """
        Checks if the matrices have the same dimensions.

        Raises:
            ValueError: If the matrices don't have the same dimensions.
        """
        if self.shape != b.shape:
            raise ValueError("The matrices don't have the same dimensions")
        
    def __getitem__(self, i:int) -> Vector:
        """Get the i-th row of the matrix.
        
        Args:
            i (int): The row index.
            
        Returns:
            Vector: The i-th row as a Vector.
        """
        return self.rows[i]
           
    
    def __add__(self, b: 'Matrix') -> 'Matrix':
        """
        Computes the sum of A_ij with B_ij with i from 0 to the number of rows, j from 0 to the number of cols
        
        Args:
            b (Matrix): The matrix to add.
        Raises:
            ValueError: If the matrices don't have the same dimensions.
        """
        self.check_dim(b)
        return Matrix([row_a + row_b for row_a, row_b in zip(self.rows, b.rows)])
    
    def __sub__(self, b: 'Matrix') -> 'Matrix':
        """
        Computes the subtraction of A_ij with B_ij with i from 0 to the number of rows, j from 0 to the number of cols
        
        Args:
            b (Matrix): The matrix to subtract.
        Raises:
            ValueError: If the matrices don't have the same dimensions.
        """
        self.check_dim(b)

        return Matrix([row_a - row_b for row_a, row_b in zip(self.rows, b.rows)])
    
    def __mul__(self, scalar: float) -> 'Matrix':
        """Multiply the matrix by a scalar.
        
        Args:
            scalar (float): The scalar value to multiply by.
            
        Returns:
            Matrix: A new matrix with all elements multiplied by the scalar.
        """
        return Matrix([row * scalar for row in self.rows])
    
    def __rmul__(self, scalar: float) -> 'Matrix':
        """Support reverse multiplication (scalar * matrix).
        
        Args:
            scalar (float): The scalar value to multiply by.
            
        Returns:
            Matrix: A new matrix with all elements multiplied by the scalar.
        """
        return self * scalar