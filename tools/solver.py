from typing import Dict


def get_coefficient(equation, i):
    c = float(equation[i - 2])
    if i > 2 and equation[i - 3] == "-":
        c *= -1
    return c


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
    coefficients: Dict[str, float] = {
        x + "^0": 0.0,
        x + "^1": 0.0,
        x + "^2": 0.0
    }
    equation = equation.split()
    if deg == 2:
        for i, var in enumerate(equation):
            if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
                coeff = get_coefficient(equation, i)
                coefficients[var] += coeff
    print(f"Coefficients are: {coefficients}")