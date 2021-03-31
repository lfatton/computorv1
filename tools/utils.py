class Utils:
    def is_number(string):
        try:
            if string.isnumeric():
                return True
            float(string)
            return True
        except ValueError:
            return False
