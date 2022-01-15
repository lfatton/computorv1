from typing import Dict
from .utils import to_power
from .utils import square_root


def get_coefficient(equation, i):
    c = float(equation[i - 2])
    if i > 2 and equation[i - 3] == "-":
        c *= -1
    return c


def get_coefficients(equation, x):
    coefficients: Dict[str, float] = {
        x + "^0": 0.0,
        x + "^1": 0.0,
        x + "^2": 0.0
    }
    for i, var in enumerate(equation):
        if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
            coefficient = get_coefficient(equation, i)
            coefficients[var] += coefficient
    print(f"Coefficients are: {coefficients}")
    return coefficients


def get_discriminant(a, b, c):
    discriminant = to_power(b, 2) - 4 * a * c
    print(f"Discriminant (b^2 - 4ac) is: {b}^2 - 4 * {a} * {c} = {discriminant}")
    return discriminant


def reduce_equation(equation, x):
    equation_left = equation[0].split()
    equation_right = equation[1].split()
    print(f"left: {equation_left} right: {equation_right}")

    for i, var in enumerate(equation_right):
        if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
            c = get_coefficient(equation_right, i)
            try:
                result = float(equation_left[equation_left.index(var) - 2]) - c
                if result < 0:
                    equation_left[equation_left.index(var) - 2] = str(result * -1)
                    if equation_left.index(var) > 2:
                        equation_left[equation_left.index(var) - 3] = "-"
                    else:
                        equation_left[0] = "-"
                else:
                    equation_left[equation_left.index(var) - 2] = str(result)
            except ValueError:
                if c < 0:
                    equation_left.insert(len(equation_left), "-")
                    c *= -1
                else:
                    equation_left.insert(len(equation_left), "+")
                equation_left.insert(len(equation_left), str(c))
                equation_left.insert(len(equation_left), "*")
                equation_left.insert(len(equation_left), var)

    equation_left.insert(len(equation_left), "=")
    equation_left.insert(len(equation_left), "0")

    return " ".join(equation_left)


def solve_equation(equation, deg, x):
    equation = equation.split()
    if deg == 2:
        coefficients = get_coefficients(equation, x)
        a = coefficients[x + "^2"]
        b = coefficients[x + "^1"]
        c = coefficients[x + "^0"]
        discriminant = get_discriminant(a, b, c)

        if discriminant < 0:
            print(f"Since discriminant is negative, there is no real solution to the equation.")
            return
        elif discriminant == 0:
            solution = -1 * b / (2 * a)
            print(f"Since discriminant is 0, there is only one solution to the equation (-b / 2a): "
                  f"-1 * {b} / (2 * {a}) =  {solution}")
        elif discriminant > 0:
            solution1 = (-1 * b + square_root(discriminant)) / (2 * a)
            solution2 = (-1 * b - square_root(discriminant)) / (2 * a)
            print(f"Since discriminant is positive, there are two real solutions to the equation"
                  f"((-b ± √discriminant) / (2a)):\n"
                  f"Solution 1: (-1 * {b} + √{discriminant}) / (2 * {a}) = {solution1}\n"
                  f"Solution 2: (-1 * {b} - √{discriminant}) / (2 * {a}) = {solution2}")



