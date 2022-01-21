import sys
import re
from .math_utils import is_number
from .parser_utils import print_usage, insert_x, insert_times_one, insert_decimal


def check_arguments(equation, x):
    regex_match = re.findall(r"[0-9" + x + "]", equation)

    if not regex_match:
        print(f"Missing variable or constants.\n")
        print_usage()

    regex_match = re.findall(r"(?!" + x + ")[A-Z]", equation)
    if regex_match:
        print(f"Too many variables or wrong variable.\n")
        print_usage()

    equation = equation.split()
    for i, var in enumerate(equation):
        if var == x + "^":
            print(f"Missing exponent.\n")
            print_usage()
    return


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

        if var == "/":
            equation = insert_decimal(equation, i)

        if any(unknown in var for unknown in [x]):
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
