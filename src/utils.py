def _validate_numbers(a, b):
    if any(isinstance(value, bool) or not isinstance(value, (int, float)) for value in (a, b)):
        raise TypeError("Both inputs must be numbers.")


def add(a, b):
    _validate_numbers(a, b)
    return a + b


def subtract(a, b):
    _validate_numbers(a, b)
    return a - b


def multiply(a, b):
    _validate_numbers(a, b)
    return a * b


def divide(a, b):
    _validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
