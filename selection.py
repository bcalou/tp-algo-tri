import random
import time


def selection_sort(seq: list[int]) -> list[int]:
    # sort the sequence by selection
    n = len(seq)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if seq[j] < seq[i]:
                min_index = j
                seq[i], seq[j] = seq[j], seq[i]


def get_time_algo(n: str):
    a = int(n)
    array: list = [random.randint(0, 100) for _ in range(a)]
    start: float = time.time()
    selection_sort(array)
    end: float = time.time()
    print("Temps écoulé pour {} entree:".format(n), end - start)

get_time_algo("1_000")
get_time_algo("2_000")
get_time_algo("3_000")
get_time_algo("10_000")
