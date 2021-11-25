import time
import random

for i in range(10):
    array = [random.randint(0, 100) for j in range(1_000*(i+1))]
    start: float = time.time()
    for j in range(len(array)):
        lowest_number = 100
        for k in range(j, len(array)):
            if array[k] < lowest_number:
                lowest_number = array[k]
                lowest_number_index = k

    end: float = time.time()
    print("Temps écoulé pour trier " +
          str(1_000*(i+1)) + " entrées :", end - start)
