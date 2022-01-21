def print_usage():
    print(f"Usage is: "
          f"python main.py equation(string) variable(optional, string)\n\n"
          f"Only natural numbers (including 0) exponents supported.\n\n"
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

    return equation


def rewrite_reduced_equation(coefficients, x, with_null_coefficients):
    a = ""
    b = ""
    c = ""

    if coefficients['a'] < 0:
        a = "- " + str(-1 * coefficients['a'])
    elif coefficients['a'] >= 0:
        a = str(coefficients['a'])
    a = a + " * " + x + "^2 "
    if coefficients['a'] == 0 and not with_null_coefficients:
        a = ""

    if coefficients['b'] < 0:
        b = "- " + str(-1 * coefficients['b'])
    elif coefficients['b'] >= 0 and a != "":
        b = "+ " + str(coefficients['b'])
    elif coefficients['b'] >= 0 and a == "":
        b = str(coefficients['b'])
    b = b + " * " + x + "^1 "
    if coefficients['b'] == 0 and not with_null_coefficients:
        b = ""

    if coefficients['c'] < 0:
        c = "- " + str(-1 * coefficients['c'])
    elif coefficients['c'] >= 0 and (a != "" or b != ""):
        c = "+ " + str(coefficients['c'])
    elif coefficients['c'] >= 0 and (a == "" and b == ""):
        c = str(coefficients['c'])
    c = c + " * " + x + "^0 "
    if coefficients['c'] == 0 and not with_null_coefficients:
        c = ""
    reduced_equation = a + b + c + "= 0"

    if len(coefficients) > 3:
        d = ""
        for i, var in enumerate(coefficients):
            if any(unknown in var for unknown in [x]):
                coefficient = coefficients[var]
                if coefficient < 0:
                    d += " - " + str(-1 * coefficient)
                elif coefficient >= 0 and d != "":
                    d += " + " + str(coefficient)
                else:
                    d += str(coefficient)
                d += " * " + str(var) + " "
        reduced_equation = d + reduced_equation

    if reduced_equation == "= 0":
        reduced_equation = "0 = 0"
        print(f"Polynomial degree: 0\n\n"
              f"Since the equation can be written as 0 = 0, all real numbers are solution.")
        exit()

    return reduced_equation
