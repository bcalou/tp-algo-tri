import time
start: float = time.time()

def factorial(number: int) -> int:
    print("Quelle est la factorielle de ", +number)
    result = 1 if number == 1 else number * factorial(number -1)

    print(result)
    return result


print(factorial(5))

end: float = time.time()
print("Temps écoulé :", end - start)