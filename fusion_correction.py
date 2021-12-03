import time
import random

def fusion_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    middle_index: int = len(array) // 2
    # Divise récursivement jusqu'a ce que le tableau soit de taille 1
    right_array = fusion_sort(array[middle_index:])
    left_array = fusion_sort(array[:middle_index])
    return merge(right_array, left_array)


def merge(left_array: list[int], right_array: list[int]) -> list[int]:
    index_left: int = 0
    index_right: int = 0

    sorted_array: list[int] = [] 
    # Parcours et tris les tableau jusqu'a arriver à la fin de l'un d'eux.
    while index_left < len(left_array) and index_right < len(right_array):
        if left_array[index_left] < right_array[index_right]:
            sorted_array.append(left_array[index_left])
            index_left += 1
        else:
            sorted_array.append(right_array[index_right])
            index_right += 1
    # Rajouter la fin du tableau dont ont est pas arrivé au bout.
    if index_left == len(left_array):
        sorted_array += right_array[index_right:]
    else:
        sorted_array += left_array[index_left:]

    # Peut aussi être écrit :
    # sorted_array += (right_array[index_right:] if index_left == len(left_array) else left_array[index_left:])

    return sorted_array

for i in range (1000, 30000, 1000):
    array = [random.randint(0, 100) for i in range(i)]
    start: float = time.time()
    fusion_sort(array)
    end: float = time.time()
    print(end - start)
