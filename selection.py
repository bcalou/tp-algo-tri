import random
import time

def sort_selection(tab: list[int]):
    for start in range(len(tab)-1):
        lowest_number: int = tab[start]
        lowest_number_index: int = start

        for i in range(start, len(tab)):
            if tab[i] < lowest_number:
                lowest_number = tab[i]
                lowest_number_index = i

        temp: int = tab[start]
        tab[start] = tab[lowest_number_index]
        tab[lowest_number_index] = temp

tableau: list[int] = [random.randint(0, 100) for _ in range(1000)]
start: float = time.time()
sort_selection(tableau)
end: float = time.time()
print("Temps écoulé pour 1 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(5000)]
start: float = time.time()
sort_selection(tableau)
end: float = time.time()
print("Temps écoulé pour 5 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(10_000)]
start: float = time.time()
sort_selection(tableau)
end: float = time.time()
print("Temps écoulé pour 10 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(20_000)]
start: float = time.time()
sort_selection(tableau)
end: float = time.time()
print("Temps écoulé pour 20 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(50_000)]
start: float = time.time()
sort_selection(tableau)
end: float = time.time()
print("Temps écoulé pour 50 000 entrées:", end - start)