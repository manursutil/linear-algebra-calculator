from __future__ import annotations


class Matrix:
    def __init__(self, rows: int, columns: int, values: list[float]) -> None:
        self.rows = rows
        self.columns = columns
        self.values: list[list[float]] = [[0] * columns for _ in range(rows)]

        if len(values) != rows * columns:
            raise ValueError(
                "The length of the values does not match the dimensions of the matrix"
            )

        k: int = 0
        for i in range(rows):
            for j in range(columns):
                self.values[i][j] = values[k]
                k += 1

    def T(self) -> Matrix:
        values: list[float] = [0] * (self.rows * self.columns)
        transposed: Matrix = Matrix(self.columns, self.rows, values)

        for i in range(self.rows):
            for j in range(self.columns):
                transposed.values[j][i] = self.values[i][j]

        return transposed

    @staticmethod
    def add(a: Matrix, b: Matrix) -> Matrix:
        if a.rows != b.rows or a.columns != b.columns:
            raise ValueError("Both matrices must have the same dimensions")

        values: list[float] = [0] * (a.rows * a.columns)
        result: Matrix = Matrix(a.rows, a.columns, values)

        for i in range(a.rows):
            for j in range(a.columns):
                result.values[i][j] = a.values[i][j] + b.values[i][j]

        return result

    def mul_scalar(self, a: float) -> Matrix:
        values: list[float] = [0] * (self.rows * self.columns)
        result: Matrix = Matrix(self.rows, self.columns, values)

        for i in range(self.rows):
            for j in range(self.columns):
                result.values[i][j] = self.values[i][j] * a

        return result

    def inverse(self) -> Matrix:
        if self.rows != self.columns:
            raise ValueError("Inverse is only defined for square matrices")

        n = self.rows
        augmented: list[list[float]] = [
            self.values[i][:] + [1.0 if i == j else 0.0 for j in range(n)]
            for i in range(n)
        ]

        for i in range(n):
            pivot_row = max(range(i, n), key=lambda r: abs(augmented[r][i]))
            pivot_value = augmented[pivot_row][i]

            if abs(pivot_value) < 1e-12:
                raise ValueError("Matrix is singular and cannot be inverted")

            if pivot_row != i:
                augmented[i], augmented[pivot_row] = augmented[pivot_row], augmented[i]

            pivot = augmented[i][i]
            for k in range(2 * n):
                augmented[i][k] /= pivot

            for j in range(n):
                if j == i:
                    continue
                factor = augmented[j][i]
                if factor == 0:
                    continue
                for k in range(2 * n):
                    augmented[j][k] -= factor * augmented[i][k]

        inverse_values = []
        for row in augmented:
            inverse_values.extend(row[n:])

        return Matrix(n, n, inverse_values)

    def det(self) -> float:
        if self.rows != self.columns:
            raise ValueError("Determinant is only defined for square matrices")

        n = self.rows
        matrix = [row[:] for row in self.values]
        determinant = 1.0

        for i in range(n):
            pivot_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
            pivot_value = matrix[pivot_row][i]

            if abs(pivot_value) < 1e-12:
                return 0.0

            if pivot_row != i:
                matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
                determinant *= -1

            determinant *= matrix[i][i]
            pivot = matrix[i][i]

            for j in range(i + 1, n):
                factor = matrix[j][i] / pivot
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]

        return determinant

    @staticmethod
    def mul(a: Matrix, b: Matrix) -> Matrix:
        if a.columns != b.rows:
            raise ValueError("The dimensions do not match")

        rows = a.rows
        columns = b.columns
        inside = a.columns

        values: list[float] = [0] * (rows * columns)
        result: Matrix = Matrix(rows, columns, values)

        for i in range(rows):
            for j in range(columns):
                for k in range(inside):
                    result.values[i][j] += a.values[i][k] * b.values[k][j]

        return result
