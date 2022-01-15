import re
from tools import parser, solver

is_natural: bool = False

argv1: str = "6 * X^2 + 3*X = 6"  # read from first argv
argv2 = "x"  # possible to enter other letter as x in 2nd argv

equation_cleaned: str = re.sub(r"[+\-*/=]", lambda char: f" {char.group(0)} ", argv1.replace(" ", "").upper())
x = argv2.upper()

if equation_cleaned.find(x + "^0") == -1:
    is_natural = True
print(f"\nIs equation in natural form? {is_natural}\n")

if is_natural:
    equation_cleaned = parser.get_unsimplified_form(equation_cleaned, x)
    print(f"Equation in non natural form: {equation_cleaned}\n")

equation_split_in_two = equation_cleaned.split(" = ")

if len(equation_split_in_two[1]) > 1:
    equation_cleaned = solver.reduce_equation(equation_split_in_two, x)

degree = parser.get_polynomial_degree(equation_cleaned)
print(f"Reduced form: {equation_cleaned}\n\n"
      f"Polynomial degree: {degree}\n")

if degree < 3:
    solver.solve_equation(equation_cleaned, degree, x)
else:
    print(f"The polynomial degree is strictly greater than 2, the equation cannot be solved.")
    exit()
