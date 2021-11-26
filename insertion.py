import time
import random

def tri_selection (tab: list[int]) -> list[int]:
    i: int = 0
    j: int = 1
    k: int = 0
    while j < len(tab):
        i = j -1
        k = tab[j]
        while i >= 0 and tab[i] > k:
            tab[i + 1] = tab[i]
            i = i - 1
        tab[i + 1] = k
        j = j + 1
    return tab

array = [random.randint(0, 100) for i in range(1000)]
start: float = time.time()
tri_selection(array)
end: float = time.time()
print("Temps écoulé :", end - start)
