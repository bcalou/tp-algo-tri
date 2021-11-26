def sort(array: list[int]) -> list[int]:
    """
    Merge sort on a list. (O(nlog(n)) complexity)
    """
    if len(array) == 1:
        return array

    # Split the list
    left: list[int] = sort(array[:int(len(array)/2)])
    right: list[int] = sort(array[int(len(array)/2):])
    return merge(left, right)


def merge(left: list[int], right: list[int]):
    """
    Merge two lists while sorting them.
    """
    mergedArray: list[int] = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            mergedArray.append(left[0])
            left.pop(0)
        else:
            mergedArray.append(right[0])
            right.pop(0)

    # Add the rest of the numbers
    if len(left) == 0:
        mergedArray += right
    else:
        mergedArray += left

    return mergedArray


if __name__ == "__main__":
    array: list[int] = [5, 8, -12, 4, 7, 0, 9]
    print("Before sort :", array)
    print("After sort :", sort(array))
