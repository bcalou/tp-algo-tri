from typing import List


"""
Le tri par selection dans un tableau consiste en :
    - Rechercher la valeur la plus petite
    - Échanger ce min avec la premiere case du tableau non trié
    - Recommencer jusqu'à ce que le tableau soit trié
"""

def basic_list_sort(unsortedList : List[int]) -> List[int]:
    if len(unsortedList) == 0:
        return unsortedList
    sortedList = unsortedList.copy()

    i : int = 0
    partial_i : int = 0
    for i in range(len(sortedList)):

        mini = sortedList[i]
        mini_i = 0

        for partial_i in range(len(sortedList[i:])):
            if mini > sortedList[i:][partial_i]:
                mini = sortedList[i:][partial_i]
                mini_i = partial_i

        sortedList[i+mini_i] = sortedList[i]
        sortedList[i] = mini

    #print("{} -> {}".format(unsortedList, sortedList))
    return sortedList
        