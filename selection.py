import time
import random
import matplotlib.pyplot as pyplot

entries = []
time_per_entry = []

for i in range(10):
    array = [random.randint(0, 100) for j in range(1_000*(i+1))]
    start: float = time.time()
    for j in range(len(array)):
        minIndex = j
        for k in range(len(array) - j):
            if array[minIndex] > array[j + k]:
                minIndex = j + k
        array[j], array[minIndex] = array[minIndex], array[j]
    end: float = time.time()
    print("Temps écoulé pour " + str(1_000*(i+1)) + " entrées :", end - start)
    goodsort = True
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            goodsort = False
            break
    if goodsort:
        print("Correct\n########################\n")
    else:
        print("False\n########################\n")

    entries.append(1_000*(i+1))
    time_per_entry.append(end - start)

pyplot.plot(entries, time_per_entry, 'ro')
pyplot.xlabel("Nombre d'entrées")
pyplot.ylabel("Temps d'exécution (en s)")
pyplot.axis([1, 11000, 0, 30])
pyplot.savefig("selection.png")
