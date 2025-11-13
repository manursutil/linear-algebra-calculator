# Linear Algebra Calculator

Small academic project for learning Python by re-implementing a handful of linear algebra routines from scratch. The focus is on understanding the algorithms (transpose, addition, scalar/matrix multiplication, determinant via Gaussian elimination, and inverse via Gauss–Jordan) rather than performance or numerical robustness.

## Running the demo

```bash
python main.py
```

This prints a few sample matrices with ASCII borders, their determinants, and — in the invertible cases — the computed inverses. Adjust `main.py` to experiment with your own matrices or extend `matrix.py` with new operations.

## GUI

Run the interactive matrix calculator:

```bash
python tkinter_gui.py
```

A basic Tkinter-based GUI lets you input matrices and perform operations like addition, multiplication, transpose, and inverse.
