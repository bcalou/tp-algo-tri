# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4! 
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!


def factorielle(number: int) -> int:
    if number == 1:
        return 1
    else:
        result = number * factorielle(number-1)
    return result

# Correction.
def factorial(number: int) -> int:
    return 1 if number == 1 else number * factorial(number-1)

print(factorielle(5))
print(factorial(5))
