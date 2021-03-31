from .utils import is_number


def insert_x0(equation, index, x):
    equation.insert(index, "*")
    equation.insert(index + 1, x + "^0")

    return equation


def insert_times_one(equation, index):
    equation.insert(index, "*")
    equation.insert(index, "1")

    return equation


def get_unsimplified_form(equation, x):
    equation = equation.split()
    print(equation)

    for i, var in enumerate(equation):
        if is_number(var):
            if i == len(equation) - 1:
                insert_x0(equation, len(equation), x)
            elif any(char in equation[i + 1] for char in ["+", "-", "="]):
                insert_x0(equation, i + 1, x)

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
