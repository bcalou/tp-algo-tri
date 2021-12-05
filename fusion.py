import random
import time

def sort(tab : list[int]) -> list[int]:
    if len(tab) <= 1: return tab

    tabLeft: list[int] = sort(tab[:int(len(tab)/2)])
    tabRight: list[int] = sort(tab[int(len(tab)/2):])

    return merge(tabLeft, tabRight)

def merge(tab1: list[int], tab2: list[int]) -> list[int]:
    tabFinal: list[int] = []

    while len(tab1) > 0 and len(tab2) > 0:

        if tab1[0] < tab2[0]:
            tabFinal.append(tab1[0])
            tab1.pop(0)
        else:
            tabFinal.append(tab2[0])
            tab2.pop(0)

    tabFinal += (tab1,tab2)[len(tab2) > 0]

    return tabFinal


# for _ in range(0,5):
#     tabTest : list[int] = [random.randint(0, 100) for _ in range(10)]
#     tabFinal: list[int] = sort(tabTest)
#     print("----------------------------------\n")
#     print(tabTest)
#     print(tabFinal)
#     print("\n----------------------------------")

tableau: list[int] = [random.randint(0, 100) for _ in range(1000)]
start: float = time.time()
sort(tableau)
end: float = time.time()
print("Temps écoulé pour 1 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(5000)]
start: float = time.time()
sort(tableau)
end: float = time.time()
print("Temps écoulé pour 5 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(10_000)]
start: float = time.time()
sort(tableau)
end: float = time.time()
print("Temps écoulé pour 10 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(20_000)]
start: float = time.time()
sort(tableau)
end: float = time.time()
print("Temps écoulé pour 20 000 entrées:", end - start)

tableau: list[int] = [random.randint(0, 100) for _ in range(50_000)]
start: float = time.time()
sort(tableau)
end: float = time.time()
print("Temps écoulé pour 50 000 entrées:", end - start)