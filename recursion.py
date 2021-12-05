def factorial(number: int) -> int:
    return factorial(number-1)*number if number != 0 else 1

print (factorial(5))