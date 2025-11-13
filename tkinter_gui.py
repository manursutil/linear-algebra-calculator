import tkinter as tk
from tkinter import messagebox

from matrix import Matrix


class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        tk.Label(self.root, text="Matrix A (rows on new lines):", font=("Arial", 24)).grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        self.txtA = tk.Text(self.root, width=30, height=10, font=("Arial", 24))
        self.txtA.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(self.root, text="Matrix B (rows on new lines):", font=("Arial", 24)).grid(
            row=0, column=1, sticky="w", padx=5, pady=5
        )
        self.txtB = tk.Text(self.root, width=30, height=10, font=("Arial", 24))
        self.txtB.grid(row=1, column=1, padx=5, pady=5)

        button_frame = tk.Frame(root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add (A+B)", command=self.add_matrices).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(
            button_frame, text="Multiply (A*B)", command=self.multiply_matrices
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Transpose A", command=self.transpose_matrix).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(button_frame, text="Inverse A", command=self.inverse_matrix).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(button_frame, text="Det(A)").pack(side=tk.LEFT, padx=5)

        tk.Label(root, text="Result:", font=("Arial", 24)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.txtResult = tk.Text(root, width=65, height=10, state="disabled", font=("Arial", 24))
        self.txtResult.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def parse_matrix(self, text: str) -> Matrix | None:
        rows = [list(map(float, line.split())) for line in text.strip().splitlines()]
        if not rows:
            messagebox.showerror("Input Error", "Matrix input is empty.")
            return None
        row_count = len(rows)
        col_count = len(rows[0])
        flat_values = [value for row in rows for value in row]
        return Matrix(row_count, col_count, flat_values)

    def add_matrices(self):
        a = self.parse_matrix(self.txtA.get("1.0", tk.END))
        b = self.parse_matrix(self.txtB.get("1.0", tk.END))
        if a and b:
            try:
                result = Matrix.add(a, b)
                self.display_result(result)
            except ValueError as e:
                messagebox.showerror("Calculation Error", str(e))

    def multiply_matrices(self):
        a = self.parse_matrix(self.txtA.get("1.0", tk.END))
        b = self.parse_matrix(self.txtB.get("1.0", tk.END))
        if a and b:
            try:
                result = Matrix.mul(a, b)
                self.display_result(result)
            except ValueError as e:
                messagebox.showerror("Calculation Error", str(e))

    def transpose_matrix(self):
        a = self.parse_matrix(self.txtA.get("1.0", tk.END))
        if a:
            transposed = a.T()
            self.display_result(transposed)

    def inverse_matrix(self):
        a = self.parse_matrix(self.txtA.get("1.0", tk.END))
        if a:
            try:
                inverse = a.inverse()
                self.display_result(inverse)
            except ValueError as e:
                messagebox.showerror("Calculation Error", str(e))

    # def calculate_determinant(self):
    #     a = self.parse_matrix(self.txtA.get("1.0", tk.END))
    #     if a:
    #         try:
    #             det = a.det()
    #             self.display_result(det)
    #         except ValueError as e:
    #             messagebox.showerror("Calculation Error", str(e))

    def display_result(self, matrix: Matrix) -> None:
        self.txtResult.config(state="normal")
        self.txtResult.delete("1.0", tk.END)
        if not matrix.values or matrix.columns == 0:
            self.txtResult.config(state="disabled")
            return

        col_widths = []
        for c in range(matrix.columns):
            col_widths.append(max(len(f"{row[c]:g}") for row in matrix.values))

        lines = []
        for row in matrix.values:
            formatted = " ".join(
                f"{value:{col_widths[i]}g}" for i, value in enumerate(row)
            )
            lines.append(formatted)

        result_str = "\n".join(lines)
        self.txtResult.insert(tk.END, result_str)
        self.txtResult.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorApp(root)
    root.mainloop()
