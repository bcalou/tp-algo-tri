import time
import random


#####
#
# Cet algorithme prend un tableau en entrée et tri les élements dans un autre croissant
# en parcourant tout le tableau
#
#####

def sort(array: list[int]) -> list[int]:
    for i in range(len(array)):
        for y in range(len(array)):
            tampon = array[i]
            if(array[y] > array[i] and array[y] > tampon):
                tampon = array[i]
                array[i] = array[y]
                array[y] = tampon
    return array


def select_order(size: int) -> list[int]:
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(size)]
    array = sort(array)
    end: float = time.time()
    print("Temps écoulé :", end - start, " pour tableau de taille", size)
    return array


select_order(1000)
select_order(2000)
select_order(3000)
select_order(4000)
select_order(5000)
select_order(6000)
select_order(7000)
select_order(8000)
select_order(9000)
select_order(10000)
