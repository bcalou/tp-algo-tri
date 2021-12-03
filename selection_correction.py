import time
import random

def selection_sort(array: list[int]) -> list[int]:
    for index, value in enumerate(array):
        permutation_index = index
        for j in range (index + 1, len(array)):
            if (value > array[j]):
                value = array[j]
                permutation_index = j
        array[index], array[permutation_index] = array[permutation_index], array[index]
    return array

#for i in range (1000, 30000, 1000):
    
# array = [random.randint(0, 100) for i in range(51000)]
# selection_sort(array)
