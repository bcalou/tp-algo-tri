import time
import random


#####
#
# Le tri par insertion prend une liste et vérifie les valeurs une par une
# en partant du premier terme est regardant si la valeur à sa gauche et plus petit si oui l'insert
# check le suivant si plus grand ou égal l'insert.
#
#####


def sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):
        y = i
        while(array[i] <= array[y] and y != -1):
            y -= 1
        array.insert(y+1, array[i])
        array.pop(i+1)
    return array


def insert_order(size: int) -> list[int]:
    start: float = time.time()
    array = [random.randint(0, 100) for i in range(size)]
    array = sort(array)
    end: float = time.time()
    print("Temps écoulé :", end - start, " pour tableau de taille", size)
    return array


insert_order(1000)
insert_order(2000)
insert_order(3000)
insert_order(4000)
insert_order(5000)
insert_order(6000)
insert_order(7000)
insert_order(8000)
insert_order(9000)
insert_order(10000)
