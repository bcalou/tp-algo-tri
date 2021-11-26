import time
import random


def sort(sort_array: list[int]) -> list[int]:
    if len(sort_array) == 1:
        return sort_array
    left_array: list[int] = sort(sort_array[:int(len(sort_array)/2)])
    right_array: list[int] = sort(sort_array[int(len(sort_array)/2):])
    return merge(left_array, right_array)


def merge(left_array: list[int], right_array: list[int]) -> list[int]:
    merged_array: list[int] = []
    while len(left_array) > 0 and len(right_array) > 0:
        if(left_array[0] > right_array[0]):
            merged_array.append(right_array[0])
            right_array.pop(0)
        else:
            merged_array.append(left_array[0])
            left_array.pop(0)
    if(len(right_array) == 0):
        merged_array += left_array
    else:
        merged_array += right_array
    return merged_array


def fusion_sort(size: int) -> list[int]:
    start: float = time.time()
    sort_array = [random.randint(0, 100) for i in range(size)]
    sort_array = sort(sort_array)
    end: float = time.time()
    print("Temps écoulé :", end - start, " pour tableau de taille", size)
    return sort_array


fusion_sort(1000)
fusion_sort(2000)
fusion_sort(3000)
fusion_sort(4000)
fusion_sort(5000)
fusion_sort(6000)
fusion_sort(7000)
fusion_sort(8000)
fusion_sort(9000)
fusion_sort(10000)
