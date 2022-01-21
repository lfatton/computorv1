def print_usage():
    print(f"Usage is: "
          f"python main.py equation(string) variable(optional, string)\n\n"
          f"Example: "
          f'python main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0" "X"')
    exit()


def insert_x(equation, index, x, power):
    equation.insert(index, "*")
    equation.insert(index + 1, x + power)

    return equation


def insert_times_one(equation, index):
    equation.insert(index, "*")
    equation.insert(index, "1")

    return equation


def insert_decimal(equation, index):
    try:
        if index == 0 or index == len(equation) - 1:
            print_usage()

        dividend = float(equation[index - 1])
        divisor = float(equation[index + 1])
        result = dividend / divisor
        equation[index] = str(result)
        del equation[index + 1]
        del equation[index - 1]
    except ValueError or IndexError:
        print_usage()
    print(equation)

    return equation


def rewrite_reduced_equation(coefficients, x):
    a = ""
    b = ""
    c = ""

    if coefficients['a'] < 0:
        a = "- " + str(-1 * coefficients['a'])
    elif coefficients['a'] > 0:
        a = str(coefficients['a'])
    a = a + " * " + x + "^2 "
    if coefficients['a'] == 0:
        a = ""

    if coefficients['b'] < 0:
        b = "- " + str(-1 * coefficients['b'])
    elif coefficients['b'] > 0 and a != "":
        b = "+ " + str(coefficients['b'])
    elif coefficients['b'] > 0 and a == "":
        b = str(coefficients['b'])
    b = b + " * " + x + "^1 "
    if coefficients['b'] == 0:
        b = ""

    if coefficients['c'] < 0:
        c = "- " + str(-1 * coefficients['c'])
    elif coefficients['c'] > 0 and (a != "" or b != ""):
        c = "+ " + str(coefficients['c'])
    elif coefficients['c'] > 0 and (a == "" and b == ""):
        c = str(coefficients['c'])
    c = c + " * " + x + "^0 "
    if coefficients['c'] == 0:
        c = ""

    reduced_equation = a + b + c + "= 0"
    if reduced_equation == "= 0":
        reduced_equation = "0 = 0"
        print(f"Reduced form: 0 = 0\n\n"
              f"Polynomial degree: 0\n\n"
              f"All reals are solution.")
        exit()

    return reduced_equation
