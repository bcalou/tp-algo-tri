import time
import random


def get_time_algo(n: str):
    a = int(n)
    array: list = [random.randint(0, 100) for _ in range(a)]
    start: float = time.time()
    list.sort(array)
    end: float = time.time()
    print("Temps écoulé pour {} entree:".format(n), end - start)

get_time_algo("1_000")
get_time_algo("2_000")
get_time_algo("3_000")
get_time_algo("10_000")
