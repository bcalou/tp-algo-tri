def factorial(number: int):
    return 1 if number == 1 else number * factorial(number - 1)

print(factorial(5))