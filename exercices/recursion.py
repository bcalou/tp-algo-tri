def factorial(value: int) -> int:
    if value == 0:
        return 1
    return factorial(value - 1) * value

        