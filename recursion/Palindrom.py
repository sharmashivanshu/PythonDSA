def is_palindrom(value):
    if len(value) == 0:
        return True
    if value[0] != value[len(value) - 1]:
        return False
    return is_palindrom(value[1:-1])

