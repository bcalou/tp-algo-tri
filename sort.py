import time
import random


def python_sort(size : int) -> list[int]:
    start: float = time.time()
    sort_array = [random.randint(0, 100) for i in range(size)]
    sort_array.sort()
    end: float = time.time()
    print("Temps écoulé :", end - start, " pour tableau de taille", size)
    return sort_array


python_sort(1000)
python_sort(2000)
python_sort(3000)
python_sort(4000)
python_sort(5000)
python_sort(6000)
python_sort(7000)
python_sort(8000)
python_sort(9000)
python_sort(10000)