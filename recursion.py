def factorial(number: int) -> int:
    if(number < 3):
        return number
    else:
        return number * factorial(number - 1)

print(factorial(5))