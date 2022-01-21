from typing import Dict
from .math_utils import to_power, square_root
from .parser_utils import rewrite_reduced_equation


def get_coefficient(equation, i):
    coefficient = float(equation[i - 2])
    if i > 2 and equation[i - 3] == "-":
        coefficient *= -1
    return coefficient


def get_coefficients(equation, x):
    coefficients: Dict[str, float] = {
        x + "^2": 0.0,
        x + "^1": 0.0,
        x + "^0": 0.0
    }

    for i, var in enumerate(equation):
        if any(unknown in var for unknown in [x]):
            coefficient = get_coefficient(equation, i)
            try:
                coefficients[var] += coefficient
            except KeyError:
                coefficients[var] = coefficient
    coefficients['a'] = coefficients.pop(x + "^2")
    coefficients['b'] = coefficients.pop(x + "^1")
    coefficients['c'] = coefficients.pop(x + "^0")

    return coefficients


def get_discriminant(a, b, c):
    discriminant = to_power(b, 2) - 4 * a * c
    print(f"Discriminant [b^2 - 4ac] is:\n"
          f"Δ = {b}^2 - 4 * {a} * {c} = {discriminant}\n")
    return discriminant


def reduce_equation(equation, x):
    equation_split_in_two = equation.split(" = ")
    equation_left = equation_split_in_two[0].split()
    equation_right = equation_split_in_two[1].split()

    left_coefficients = get_coefficients(equation_left, x)
    right_coefficients = get_coefficients(equation_right, x)
    coefficients = left_coefficients

    for i, var in enumerate(right_coefficients):
        try:
            coefficients[var] = left_coefficients[var] - right_coefficients[var]
        except KeyError:
            coefficients[var] = right_coefficients[var]

    reduced_equation = rewrite_reduced_equation(coefficients, x)

    return reduced_equation


def solve_equation(equation, deg, x):
    equation = equation.split()
    coefficients = get_coefficients(equation, x)

    if deg == 0:
        print(f"\n{coefficients['c']} cannot be equal to 0.\n\n"
              f"There is no solution.")
        exit()

    if deg == 1:
        solution = -1 * coefficients['c'] / coefficients['b']
        print(f"The equation is linear.\n\n"
              f"The solution is:\n"
              f"{x} = -1 * {coefficients['c']} / {coefficients['b']} = {solution}\n")
        exit()

    if deg == 2:
        print(f"The equation is quadratic.\n"
              f"Coefficients are: {coefficients}\n")
        discriminant = get_discriminant(coefficients['a'], coefficients['b'], coefficients['c'])

        if discriminant < 0:
            print(f"Since the discriminant is negative, there is no real solution to the equation.\n")
            exit()
        elif discriminant == 0:
            solution = -1 * coefficients['b'] / (2 * coefficients['a'])
            print(f"Since the discriminant is 0, there is only one solution to the equation [-b / 2a]: "
                  f"{x} = -1 * {coefficients['b']} / (2 * {coefficients['a']}) =  {solution}\n")
            exit()
        elif discriminant > 0:
            x1 = (-1 * coefficients['b'] + square_root(discriminant)) / (2 * coefficients['a'])
            x2 = (-1 * coefficients['b'] - square_root(discriminant)) / (2 * coefficients['a'])
            print(f"Since the discriminant is positive, there are two real solutions to the equation "
                  f"[(-b ± √Δ) / (2a)]:\n"
                  f"{x}1 = (-1 * {coefficients['b']} + √{discriminant}) / (2 * {coefficients['a']}) = {x1}\n"
                  f"{x}2 = (-1 * {coefficients['b']} - √{discriminant}) / (2 * {coefficients['a']}) = {x2}\n")
            exit()
