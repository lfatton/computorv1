import re
from tools import parser, solver

is_natural: bool = False

argv1: str = "5 + 4.8 * X^2 = -2 * X^2 + X"  # read from first argv
argv2 = "x"  # possible to enter other letter as x in 2nd argv

equation_cleaned: str = re.sub(r"[+\-*/=]", lambda char: f" {char.group(0)} ", argv1.replace(" ", "").upper())
x = argv2.upper()

if equation_cleaned.find(x + "^0") == -1:
    is_natural = True
print(f"Is equation in natural form? {is_natural}")

if is_natural:
    equation_cleaned = parser.get_unsimplified_form(equation_cleaned, x)
print(f"equation cleaned: {equation_cleaned} and unknown: {x}")

equation_split_in_two = equation_cleaned.split(" = ")
print(f"equation split in two: {equation_split_in_two}")

if len(equation_split_in_two[1]) > 1:
    equation_cleaned = solver.reduce_equation(equation_split_in_two, x)

degree = parser.get_polynomial_degree(equation_cleaned)
print(f"Reduced form: {equation_cleaned}\n"
      f"Polynomial degree: {degree}")

if degree < 3:
    solver.solve_equation(equation_cleaned, degree, x)
else:
    print(f"The polynomial degree is strictly greater than 2, I can't solve.")
