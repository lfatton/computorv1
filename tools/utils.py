def is_number(var):
    try:
        if var.isnumeric():
            return True
        float(var)
        return True
    except ValueError:
        return False
