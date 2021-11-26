def sort(array: list[int]) -> list[int]:
    """
    Sorting a list by insertion (O(n²) complexity)
    """
    for start in range(len(array)):
        current_number: int = array[start]
        i = start-1
        while i > -1 and current_number < array[i]:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = current_number
    return array

if __name__ == "__main__":
    array: list[int] = [5, 8, -12, 4, 7, 0]
    print("Before sort :", array)
    print("After sort :", sort(array))
