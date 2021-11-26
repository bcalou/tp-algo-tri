def merge(left_array: list[int], right_array: list[int]) -> list[int]:
    print("merge : ", left_array, right_array)
    index_left: int = 0
    index_right: int = 0
    sorted_array: list[int] = []
    while index_left < len(left_array) and index_right < len(right_array):
        if left_array[index_left] < right_array[index_right]:
            sorted_array.append(left_array[index_left])
            index_left += 1
        else:
            sorted_array.append(right_array[index_right])
            index_right += 1

    # sorted_array += (right_array[index_right:] if index_left == len(left_array) else left_array[index_left:])

    if index_left == len(left_array):
        sorted_array += right_array[index_right:]
    else:
        sorted_array += left_array[index_left:]
    return sorted_array

def sort(array: list[int]) -> list[int]:
    print("sort : ", array)
    if len(array) <= 1:
        return array
    middle_index: int = len(array)//2
    right_array: list[int] = sort(array[middle_index:])
    left_array: list[int] = sort(array[:middle_index])
    return merge(right_array, left_array)


print(sort([3, 9, 8, 12,117, 19283, 13732, 363,2, 6]))
