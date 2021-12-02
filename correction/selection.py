import random


def sort(array: list[int]) -> list[int]:

    # For each item of the input array
    for index in range(len(array)):

        # For now, assume that the current element is the smallest
        smallestIndex: int = index

        # For each element between the current element and the end of the array
        # (that is the unsorted part of the array)
        for j in range(index, len(array)):

            # If the element is smaller than the smallest so far,
            # it becomes the new smallest
            if array[j] < array[smallestIndex]:
                smallestIndex = j

        # Exchange the position of the current element and the smallest element
        # found in the rest of the array
        array[index], array[smallestIndex] = array[smallestIndex], array[index]

    return array

array = [random.randint(0, 100) for i in range(10)]
print(sort(array))
