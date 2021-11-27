from typing import List

def insertion_sort(unsortedList : List[int]) -> List[int]:
    if len(sortedList) <= 1:
        return sortedList
    sortedList = unsortedList.copy()

    for i in range(1, len(sortedList)):
        reverse_index = i - 1 
        while sortedList[i] < sortedList[reverse_index] and reverse_index >= 0:
            reverse_index -=  1
        val = sortedList.pop(i)
        sortedList.insert(reverse_index + 1, val)

    return sortedList
        