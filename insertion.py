import time
import random

def insertion_sort(array: list[int]) -> list[int]:
    start: float = time.time()
    for index in range(1, len(array)):
        start_value: int = array[index]
        current_index: int = index - 1
        while current_index >= 0 and start_value < array[current_index] :
            array[current_index + 1] = array[current_index]
            current_index -= 1
        array[current_index + 1] = start_value
    end: float = time.time()
    print(end - start)
    return array


for i in range (1000, 30000, 1000):
    array = [random.randint(0, 100) for i in range(i)]
    insertion_sort(array)
