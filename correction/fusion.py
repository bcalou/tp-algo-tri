import random


def merge(leftArray: list[int], rightArray: list[int]):
    """Merge two sorted arrays into an array that will also be sorted
    Exemple: merge([1, 5], [3, 6]) will result in [1, 3, 5, 6]
    """
    # The final array
    array: list[int] = []

    # Keep a trace of where we are in each sub-array
    leftIndex = rightIndex = 0

    # While there are still element in the input tables
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):

        # If the element of the left array is the smaller one, append it
        if (leftArray[leftIndex] < rightArray[rightIndex]):
            array.append(leftArray[leftIndex])

            # Move the index of the left array for the next comparaison
            leftIndex += 1
        
        # Else use the element from the right array
        else:
            array.append(rightArray[rightIndex])
            rightIndex += 1

    # After the while loop, only one of the array remains
    # Append the remaining array to the final array
    if leftIndex < len(leftArray):
        array += leftArray[leftIndex:]
    else:
        array += rightArray[rightIndex:]

    return array


def sort(array: list[int]) -> list[int]:
    """Sort the given array
    Each time the array is more than one element, divide it into a shorter
    list and call recursively sort()
    """

    if len(array) <= 1:
        return array

    middle: int = len(array) // 2

    leftArray: list[int] = sort(array[middle:])
    rightArray: list[int] = sort(array[:middle])

    return merge(leftArray, rightArray)


array = [random.randint(0, 100) for i in range(10)]
print(sort(array))
