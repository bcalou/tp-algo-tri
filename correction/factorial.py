def factorial(number: int) -> int:
    return 1 if number == 1 else number * factorial(number - 1)

# Exemple with factorial(3) which is 3 * 2 * 1 = 6

# factorial(3) is called
# 3 is not 1. So we want 3 * factorial(2)

    # factorial(2) is called
    # 2 is not 1. So we want 2 * factorial(1)

        # factorial(1) is called
        # We know that factorial(1) is 1, so return 1 !

    # factorial(1) has returned 1.
    # 2 * 1 = 2
    # Return 2 !

# factorial(2) has returned 2.
# 3 * 2 = 6
# Return 6 !