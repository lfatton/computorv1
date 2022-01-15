def is_number(var):
    try:
        if var.isnumeric():
            return True
        float(var)
        return True
    except ValueError:
        return False


def to_power(number, power):
    result = number

    if power == 0:
        return 1
    if power < 0:
        return 1 / to_power(number, power * -1)
    for i in range(power - 1):
        result *= number
    return result


# using Babylonian method
def square_root(number):
    if number < 0:
        print(f"Error: negative square root!")
        exit(-1)
    if number == 0:
        return 0
    if number == 4:
        return 2.0

    error = 0.0000001
    n = (number + 1) / 2
    n1 = (n + number / n) / 2
    while (n - n1) > error:
        n = n1
        n1 = (n1 + number / n1) / 2
    return n1
