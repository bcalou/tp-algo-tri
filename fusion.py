import time
import random
import matplotlib.pyplot as pyplot

entries = []
time_per_entry = []


def merge(array1: list[int], array2: list[int]) -> list[int]:
    merged_array = []
    for i in range(len(array1) + len(array2)):
        if array1[0] <= array2[0]:
            merged_array.append(array1[0])
            del array1[0]
            if len(array1) == 0:
                for j in array2:
                    merged_array.append(j)
                break
        else:
            merged_array.append(array1[0])
            del array2[0]
            if len(array2) == 0:
                for j in array1:
                    merged_array.append(j)
                break
    return merged_array


def sort(array: list[int]) -> list[int]:
    if len(array) > 1:
        array_first_half = array[0:(len(array)//2)]
        array_second_half = array[(len(array)//2):len(array)]
        return merge(sort(array_first_half), sort(array_second_half))

    return array


time_passed: float = 0
for i in range(10):
    array = [random.randint(0, 100) for j in range(10_000*(i+1))]
    start: float = time.time()
    array = sort(array)
    end: float = time.time()
    time_passed = end - start
    print("Temps écoulé pour " + str(10_000*(i+1)) + " entrées :", time_passed)
    goodsort = True
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            goodsort = False
            break
    if goodsort:
        print("Correct\n########################\n")
    else:
        print("False\n########################\n")

    entries.append(10_000*(i+1))
    time_per_entry.append(time_passed)


pyplot.plot(entries, time_per_entry, 'ro')
pyplot.xlabel("Nombre d'entrées")
pyplot.ylabel("Temps d'exécution (en s)")
pyplot.axis([1, 100_000, 0, time_passed])
pyplot.savefig("fusion.png")
