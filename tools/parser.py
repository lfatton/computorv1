from .math_utils import is_number
from .parser_utils import insert_x, insert_times_one


def get_unsimplified_form(equation, x):
    equation = equation.split()

    for i, var in enumerate(equation):
        if is_number(var):
            if i == len(equation) - 1:
                insert_x(equation, len(equation), x, "^0")
            elif any(char in equation[i + 1] for char in ["+", "-", "="]):
                insert_x(equation, i + 1, x, "^0")

        if var == x:
            equation[i] = x + "^1"

        if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
            if i == 0:
                insert_times_one(equation, 0)
            elif equation[i - 1] != "*":
                insert_times_one(equation, i)

    return " ".join(equation)


def get_polynomial_degree(equation):
    deg = 0
    for i, char in enumerate(equation):
        if char == "^" and int(equation[i + 1]) > deg:
            deg = int(equation[i + 1])

    return deg
