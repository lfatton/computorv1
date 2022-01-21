import re
import sys
from tools import parser, solver

is_natural: bool = False

if len(sys.argv) > 3:
    parser.print_usage()
if len(sys.argv) > 2:
    if len(sys.argv[2]) == 1 and re.match("[A-Za-z]", sys.argv[2]):
        x = sys.argv[2].upper()
    else:
        parser.print_usage()
else:
    x = "X"
if len(sys.argv) > 1:
    equation = re.sub(r"[+\-*/=]", lambda char: f" {char.group(0)} ", sys.argv[1].replace(" ", "").upper())
    parser.check_arguments(equation, x)
else:
    parser.print_usage()


if equation.find(x + "^0") == -1 or equation.find("/") != -1:
    is_natural = True
print(f"\nIs equation in natural form? {is_natural}\n")

if is_natural:
    equation = parser.get_unsimplified_form(equation, x)
    print(f"Equation in non natural form: {equation}\n")

equation = solver.reduce_equation(equation, x)

degree = parser.get_polynomial_degree(equation)
print(f"Reduced form: {equation}\n\n"
      f"Polynomial degree: {degree}")

if degree < 3:
    solver.solve_equation(equation, degree, x)
else:
    print(f"The polynomial degree is strictly greater than 2, the equation cannot be solved.")
    exit()
