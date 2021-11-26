import time
import random

def tri_selection (tab: list[int]) -> list[int]:
    i: int = 0
    j: int = 0
    min: int = 0
    min_numbers: int
    # Itération dans le tableau
    while i < len(tab):
        j = i + 1
        min = i
        # Tant que j < a la taille du tableau, si la valeur en j est inferieur a la valeur en min alors min = j
        while j < len(tab):
            if tab[j] < tab[min]:
                min =  j
            j = j + 1
        # Si i et min ne sont pas les même alors on echange leur contenus
        if min != i:
            min_numbers = tab[i]
            tab[i] = tab[min]
            tab[min] = min_numbers
        i = i + 1
    return tab

array = [random.randint(0, 100) for i in range(10000)]
start: float = time.time()
tri_selection(array)
end: float = time.time()
print("Temps écoulé :", end - start)