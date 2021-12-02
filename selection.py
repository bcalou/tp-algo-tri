import random
import time

array = [random.randint(0, 100) for i in range(100)]

array2 = [0,1,2,6,1,0,15,12,3,8,9]

array3 = [77,75,72,70,60,52,41,3,2,21,21,10]

def selection_sort(array: list[int]) -> list[int]:
    #on parcourt tous les éléments du tableau
    for i in range(len(array)):
        #pour chaque élement on parcours la suite du tableau
        permut_index = i
        for j in range(i, len(array)):
            #si on en trouve un plus petit que celui conservé on
            #prend son index à la place
            if array[j] < array[permut_index]:
                permut_index = j
        #une fois à la fin on permutte le plus petit nombre trouvé avec
        #le premier sélectionné
        array[i], array[permut_index] = array[permut_index], array[i]

    return array

start: float = time.time()

selection_sort(array)

end: float = time.time()

print(selection_sort(array3))
print("Temps écoulé :", end - start)
