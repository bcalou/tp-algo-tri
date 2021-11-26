from fusion import sort
import random


def check_sort() -> bool:
    array : list = [random.randint(0, 100) for i in range(100)]
    array = sort(array)

    for i in range(1, len(array)):
        if  array[i] < array[i - 1]:
            return False
    return True

print('\033[92m✓ OK' if check_sort() else '\033[91m❌KO')
