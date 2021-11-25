import time
import random
import matplotlib.pyplot as pyplot

entries = []
time_per_entry = []

for i in range(10):
    array = [random.randint(0, 100) for j in range(2_000*(i+1))]
    start: float = time.time()
    for j in range(len(array)):
        insertIndex = j
        for k in range(j):
            if array[insertIndex] < array[k]:
                insertIndex = k
                break
        array.insert(insertIndex, array[j])
        del array[j+1]
    end: float = time.time()
    print("Temps écoulé pour " + str(2_000*(i+1)) + " entrées :", end - start)
    goodsort = True
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            goodsort = False
            break
    if goodsort:
        print("Correct\n########################\n")
    else:
        print("False\n########################\n")

    entries.append(2_000*(i+1))
    time_per_entry.append(end - start)

pyplot.plot(entries, time_per_entry, 'ro')
pyplot.xlabel("Nombre d'entrées")
pyplot.ylabel("Temps d'exécution (en s)")
pyplot.axis([1, 21000, 0, 40])
pyplot.savefig("insertion.png")
