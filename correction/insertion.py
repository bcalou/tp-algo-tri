import random


def sort(array: list[int]) -> list[int]:

    # For each item of the input array
    for index, element in enumerate(array):

        # Current element position
        # We will modify this value until we find the new correct position
        elementPosition: int = index

        # Start from the current item an go back to the beginning
        # While we've not reach the beginning of the array and
        # the element on the left is higher
        while elementPosition > 0 and array[elementPosition - 1] > element:

            # Move the element that is higher to the right
            array[elementPosition] = array[elementPosition - 1]

            # Decrement the elementPosition before the next while iteration
            elementPosition -= 1

        # Now we found the wanted element position, move it there
        array[elementPosition] = element

    return array

array = [random.randint(0, 100) for i in range(10)]
print(sort(array))
