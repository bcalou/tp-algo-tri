def factorial(n: int) -> int:
    if n <= 2:
        return n
    return n * factorial(n-1)


for i in range(10):
    print("la factorielle de " + str(i+1) + " est " + str(factorial(i+1)))
