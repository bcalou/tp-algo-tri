import random
import time

array = [random.randint(0, 100) for i in range(10)]
print(array)
def insertion_sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):
        start_value = array[i]
        current_index = i - 1
        while current_index >= 0 and start_value < array[current_index]:
            array[current_index + 1] = array[current_index]
            current_index -= 1
        array[current_index + 1] = start_value
    print(array)
    return array

insertion_sort(array)