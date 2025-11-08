from matrix import Matrix


def print_matrix(matrix: Matrix) -> None:
    cell_width = max(len(f"{value:g}") for row in matrix.values for value in row)
    horizontal = "+" + "+".join(["-" * (cell_width + 2)] * matrix.columns) + "+"

    print(horizontal)
    for row in matrix.values:
        formatted = " | ".join(f"{value:>{cell_width}g}" for value in row)
        print(f"| {formatted} |")
        print(horizontal)


def print_section(title: str, matrix: Matrix) -> None:
    print(f"### {title}")
    print_matrix(matrix)
    print()


def main() -> None:
    a = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print_section("Matrix A", a)
    print(f"det(A) = {a.det()}\n")
    try:
        print_section("Inverse of A", a.inverse())
    except ValueError as exc:
        print(f"Inverse of A: {exc}\n")

    b = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    print_section("Matrix B", b)
    print_section("Matrix B Transposed", b.T())

    c = Matrix(3, 2, [2, 1, 4, 5, 5, 4])
    print_section("B + C", Matrix.add(b, c))
    print_section("Matrix B × 2", Matrix.mul_scalar(b, 2))

    print_section("B Transposed x C", Matrix.mul(b.T(), c))

    d = Matrix(3, 3, [2, 1, 0, 0, 1, -1, 1, 0, 1])
    print_section("Matrix D", d)
    print(f"det(D) = {d.det()}\n")
    print_section("Inverse of D", d.inverse())


if __name__ == "__main__":
    main()
