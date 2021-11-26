def sort(array: list[int]) -> list[int]:
    """
    Sorting a list by selection (O(n²) complexity)
    """
    for start in range(len(array)-1):
        # Search lowest value in rest of the array
        lowest_number: int = array[start]
        lowest_number_index: int = start
        for i in range(start, len(array)):
            if array[i] < lowest_number:
                lowest_number = array[i]
                lowest_number_index = i

        # Replace value by lowest
        array[start], array[lowest_number_index] = array[lowest_number_index], array[start]

    return array

if __name__ == "__main__":
    array: list[int] = [5, 8, -12, 4, 7, 0]
    print("Before sort :", array)
    print("After sort :", sort(array))
