def is_number(string):
    try:
        if string.isnumeric():
            return True
        float(string)
        return True
    except ValueError:
        return False


def insert_x0(equation, index):
    global x
    equation.insert(index, "*")
    equation.insert(index + 1, x + "^0")
    return equation


def insert_times_one(equation, index):
    equation.insert(index, "*")
    equation.insert(index, "1")
    return equation


def get_unsimplified_form(equation):
    global x
    equation = equation.split()
    print(equation)

    for i, var in enumerate(equation):
        if is_number(var):
            if i == len(equation) - 1:
                insert_x0(equation, len(equation))
            elif any(char in equation[i + 1] for char in ["+", "-", "="]):
                insert_x0(equation, i + 1)

        if var == x:
            equation[i] = x + "^1"

        if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
            if i == 0:
                insert_times_one(equation, 0)
            elif equation[i - 1] != "*":
                insert_times_one(equation, i)

    return " ".join(equation)


def get_determinant(equation, i):
    det = float(equation[i - 2])
    if det > 2 and equation[i - 3] == "-":
        det *= -1
    return det


def reduce_equation(equation):
    equation_left = equation[0].split()
    equation_right = equation[1].split()
    print(f"left: {equation_left} right: {equation_right}")

    for i, var in enumerate(equation_right):
        if any(unknown in var for unknown in [x + "^2", x + "^1", x + "^0", x]):
            det = get_determinant(equation_right, i)
            try:
                result = float(equation_left[equation_left.index(var) - 2]) - det
                if result < 0:
                    equation_left[equation_left.index(var) - 2] = str(result * -1)
                    if equation_left.index(var) > 2:
                        equation_left[equation_left.index(var) - 3] = "-"
                    else:
                        equation_left[0] = "-"
                else:
                    equation_left[equation_left.index(var) - 2] = str(result)
            except ValueError:
                if det < 0:
                    equation_left.insert(len(equation_left), "-")
                    det *= -1
                else:
                    equation_left.insert(len(equation_left), "+")
                equation_left.insert(len(equation_left), str(det))
                equation_left.insert(len(equation_left), "*")
                equation_left.insert(len(equation_left), var)

    equation_left.insert(len(equation_left), "=")
    equation_left.insert(len(equation_left), "0")

    return " ".join(equation_left)


def get_polynomial_degree(equation):
    deg = 0
    for i, char in enumerate(equation):
        if char == "^" and int(equation[i + 1]) > deg:
            deg = int(equation[i + 1])

    return deg


def solve_equation(equation, deg):
    if deg == 2:
        print(f"{equation.split()}")


is_natural = False

argv1 = "5 + 4.8 * X^2 = -2 * X^2 + X"  # read from first argv
argv2 = "x"  # possible to enter other letter as x in 2nd argv

equation_cleaned = "".join(argv1.split()).upper() \
    .replace("+", " + ") \
    .replace("-", " - ") \
    .replace("*", " * ") \
    .replace("=", " = ")
x = argv2.upper()

determinants = {
    x + "^0": 0.0,
    x + "^1": 0.0,
    x + "^2": 0.0
}

if equation_cleaned.find(x + "^0") == -1:
    is_natural = True
print(f"Is equation in natural form? {is_natural}")

if is_natural:
    equation_cleaned = get_unsimplified_form(equation_cleaned)
print(f"equation cleaned: {equation_cleaned} and unknown: {x}")

equation_split_in_two = equation_cleaned.split(" = ")
print(f"equation split in two: {equation_split_in_two}")

if len(equation_split_in_two[1]) > 1:
    equation_cleaned = reduce_equation(equation_split_in_two)

degree = get_polynomial_degree(equation_cleaned)
print(f"Reduced form: {equation_cleaned}\n"
      f"Polynomial degree: {degree}")

if degree < 3:
    solve_equation(equation_cleaned, degree)
else:
    print(f"The polynomial degree is strictly greater than 2, I can't solve.")
