def factorial(number: int) -> int:
    if number > 1:
        return factorial(number - 1) * number
    elif number == 0:
        return 1
    else:
        return number

print(factorial(10))