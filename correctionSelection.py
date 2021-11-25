import random

array = [random.randint(0, 100) for i in range(10)]

print(array)

def selection_sort(array: list[int]) -> list[int]:
    for i, value in enumerate(array):
        permutation_index = i
        for j in range (i + 1, len(array)):
            if (value > array[j]):
                value = array[j]
                permutation_index = j
        array[i], array[permutation_index] = array[permutation_index], array[i]
    return array
    #NE PAS OUBLIER LES ESPACES

print(selection_sort(array))