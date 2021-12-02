import random
import time

array = [random.randint(0, 100) for i in range(10)]

array2 = [0,1,2,6,1,0,15,12,3,8,9]

def insertion_sort(array: list[int]) -> list[int]:
    #on parcourt tous les éléments du tableau
    for i in range(1, len(array)):
        #pour chaque valeur on parcours tous les élements après lui
        start_value = array[i]
        current_index = i - 1

        #on parcours tous les nombres avant celui sélectionné
        #(ceux d'avant sont déjà trié)
        #dès qu'il tombe sur un plus petit on le place devant lui
        #et on avance tous les nombres plus grand d'un index
        while current_index >= 0 and start_value < array[current_index]:
            array[current_index + 1] = array[current_index]
            current_index -= 1
        array[current_index + 1] = start_value

    return array

start: float = time.time()

insertion_sort(array)

end: float = time.time()

print("Temps écoulé :", end - start)
