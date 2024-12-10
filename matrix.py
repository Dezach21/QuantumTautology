class Matrix:
    def __init__(self, data) -> None:
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

        # Verifies all rows have the same number of elements.
        if not all(len(row) == self.cols for row in self.data):
            raise ValueError("Invalid matrix. All rows must have the same number of elements.")

        # Verifies all elements are of type int, float, or complex.
        for row in self.data:
            for element in row:
                if not isinstance(element, (int, float, complex)):
                    raise ValueError("Invalid matrix. All elements must be of type int, float, or complex.")

    def __getitem__(self, index: int) -> list:
        return self.data[index]

    def __setitem__(self, index: int, value: int | float | complex) -> None:
        self.data[index] = value

    def __repr__(self) -> repr:
        return repr(self.data)

    def __eq__(self, other: "Matrix") -> bool:
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data

    def __mul__(self, scalar: int | float | complex) -> "Matrix":
        if not isinstance(scalar, (int, float, complex)):
            raise TypeError("Invalid type for scalar-matrix multiplication")

        result = fill_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] * scalar

        return result

    def __rmul__(self, scalar: int | float | complex) -> "Matrix":
        return self.__mul__(scalar)

    def __matmul__(self, second_matrix: "Matrix") -> "Matrix":
        if self.cols != second_matrix.rows:
            raise ValueError("Incompatible dimensions for matrix multiplication.")
        if not isinstance(second_matrix, Matrix):
            raise TypeError("Invalid type for matrix-matrix multiplication.")

        result = fill_matrix(self.rows, second_matrix.cols)

        for i in range(self.rows):
            for j in range(second_matrix.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * second_matrix.data[k][j]

        return result

    def __truediv__(self, scalar: int | float | complex) -> "Matrix":
        if not isinstance(scalar, int | float | complex):
            raise TypeError("Invalid type for matrix-scalar division.")

        result = fill_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] / scalar

        return result

    def __add__(self, second_matrix: "Matrix") -> "Matrix":
        if not isinstance(second_matrix, Matrix):
            raise TypeError("Invalid type for matrix-matrix addition.")
        if self.rows != second_matrix.rows or self.cols != second_matrix.cols:
            raise ValueError("Incompatible dimensions for matrix addition.")

        result = fill_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] + second_matrix.data[i][j]

        return result

    def __sub__(self, second_matrix: "Matrix") -> "Matrix":
        if not isinstance(second_matrix, Matrix):
            raise TypeError("Invalid type for matrix-matrix subtraction.")
        if self.rows != second_matrix.rows or self.cols != second_matrix.cols:
            raise ValueError("Incompatible dimensions for matrix subtraction.")

        result = fill_matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self.data[i][j] - second_matrix.data[i][j]

        return result

    def transpose(self) -> "Matrix":
        """Transpose a matrix."""
        return Matrix([[row[column] for row in self.data] for column in range(self.cols)])

    def invert(self) -> "Matrix":
        """Invert a matrix."""
        identity, inverse = identity_matrix(self.rows), list()

        for i in range(self.rows):
            # Solve for each column of the identity matrix.
            column = zip_lists_to_matrix([row[i] for row in identity])
            inverse_column = gepp(self.data, column).transpose()[0]
            inverse.append(inverse_column)

        return Matrix(inverse).transpose()

    def determinant(self) -> float:
        """Determinant of a matrix."""
        if self.rows != self.cols:
            raise ValueError("Incompatible dimensions for matrix determinant.")

        det = 0.0
        for column in range(self.cols):
            sub_matrix = Matrix([[self.data[row][col] for col in range(self.cols) if col != column]
                                 for row in range(self.rows) if row != 0])
            det += (-1) ** column * self.data[0][column] * sub_matrix.determinant()

        return det


def fill_matrix(rows: int, cols: int, value: int | float | complex = 0) -> Matrix:
    """
    Create a matrix filled with `value`, with given number of rows and columns.

    :param rows: The number of rows.
    :param cols: The number of columns.
    :param value: The value to fill the matrix with.
    :return: A ``rows``-by-``cols`` matrix filled with `value`.
    """
    return Matrix([[value for _ in range(cols)] for _ in range(rows)])


def identity_matrix(size: int) -> Matrix:
    """
    Create a matrix of dimensions ``size``-by-``size`` filled with zeroes except the diagonal filled with ones.

    :param size: The dimension of the square matrix.
    :return: A square matrix with a diagonal filled with ones.
    """
    identity = fill_matrix(size, size)

    for i in range(size):
        for j in range(size):
            identity[i][j] += 1 * (i == j)

    return identity


def zip_lists_to_matrix(*lists: list) -> Matrix:
    """
    Create a matrix from a list of lists. Each list is considered as a column.

    :param lists: A list of lists.
    :return: A `l`-by-`n` matrix, where `l` is the length of the lists, and `n` the number of lists.
    """
    for i in lists:
        if len(i) != len(lists[0]):
            raise ValueError("All lists must have the same length.")

    zipped_data = [list(row) for row in zip(*lists)]

    return Matrix(zipped_data)


def gepp(a: Matrix, b: Matrix) -> Matrix:
    """
    Solve the system of equations `ax = b` using Gaussian elimination with partial pivoting.
    Implementation based on `<https://www.cs.mcgill.ca/~chang/teaching/cs350/slides/le.pdf>`_.

    :param a: A non-singular `n`-by-`n` matrix.
    :param b: A `n`-by-`1` matrix.
    :return: The solution `x`, a `1`-by-`n` matrix.
    """
    n = b.rows
    solution = fill_matrix(n, 1)

    for k in range(n):
        sub_column = [abs(a[r][k]) for r in range(k, n)]
        max_val = max(sub_column)
        max_index = sub_column.index(max_val) + k

        if max_val == 0:
            raise ValueError("Invalid matrix. The matrix must not be singular.")

        a[k][0], a[max_index][0] = a[max_index][0], a[k][0]
        b[k][0], b[max_index][0] = b[max_index][0], b[k][0]

        for i in range(k + 1, n):
            mult = a[i][k] / a[k][k]
            a[i][k:] = [a[i][c] - mult * a[k][c] for c in range(k, n)]
            b[i][0] = b[i][0] - mult * b[k][0]

        for j in range(n - 1, -1, -1):
            solution[j][0] = (b[j][0] - sum(a[j][c] * solution[c][0] for c in range(j + 1, n))) / a[j][j]

    return solution


def embed(small_matrix: Matrix | int | float | complex, large_matrix: Matrix | int) -> Matrix:
    """
    Embed ``small_matrix`` into the lower right corner of ``large_matrix``. If no ``large_matrix`` is given, but instead
    an integer, an identity matrix is used as ``large_matrix``.

    :param small_matrix: A smaller matrix to embed, or a scalar to specify a `1`-by-`1` matrix.
    :param large_matrix: A larger matrix to receive the embedding, or an integer to specify an identity matrix.
    :return: A new matrix with the embedded smaller matrix in the lower right corner.
    """
    if isinstance(large_matrix, int):
        large_matrix = identity_matrix(large_matrix)
    if isinstance(small_matrix, int | float | complex):
        small_matrix = Matrix([[small_matrix]])

    embedded_matrix = Matrix([row[:] for row in large_matrix.data])  # Copy to avoid changing the original.

    if small_matrix.rows > large_matrix.rows or small_matrix.cols > large_matrix.cols:
        raise ValueError("The dimensions of the small matrix must fit within the large matrix.")

    for i in range(small_matrix.rows):
        for j in range(small_matrix.cols):
            embedded_matrix[large_matrix.rows - small_matrix.rows + i][
                large_matrix.cols - small_matrix.cols + j] = small_matrix[i][j]

    return embedded_matrix
