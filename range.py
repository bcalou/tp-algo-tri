import random
import time


def get_time_algo(n: str):
    a = int(n)
    start: float = time.time()
    array: list = [random.randint(0, 100) for _ in range(a)]
    end: float = time.time()
    print("Temps écoulé pour {} entree:".format(n), end - start)

get_time_algo("1_000_000")
get_time_algo("2_000_000")
get_time_algo("3_000_000")
get_time_algo("10_000_000")
