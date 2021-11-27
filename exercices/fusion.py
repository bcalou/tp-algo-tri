from typing import List


def fusion_sort(unsortedList : List[int]) -> List[int]:
    if len(unsortedList) <= 1:
        return unsortedList
    sortedList = unsortedList.copy()

    medianIndex = len(sortedList) // 2

    halfLeft = fusion_sort(sortedList[:medianIndex])
    halfRight = fusion_sort(sortedList[medianIndex:])

    result = list_fusion(halfLeft.copy(), halfRight.copy())
    return result

def list_fusion(list1 : List[int], list2 : List[int]):
    fusedList = []

    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            fusedList.append(list1.pop(0))
        else:
            fusedList.append(list2.pop(0))
    
    while len(list1) != 0:
        fusedList.append(list1.pop(0))
    while len(list2) != 0:
        fusedList.append(list2.pop(0))
    
    return fusedList

        