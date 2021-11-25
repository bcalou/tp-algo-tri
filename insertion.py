import random
import time


def insert_sort(seq: list[int]) -> list[int]:
    # sort the sequence by insertion
    n = len(seq)
    # from the first element to the end
    for i in range(1, n):
        # search the element less than the current one from the position current to the begin
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j-1], seq[j] = seq[j], seq[j-1]


def get_time_algo(n: str):
    a = int(n)
    array: list = [random.randint(0, 100) for _ in range(a)]
    start: float = time.time()
    insert_sort(array)
    end: float = time.time()
    print("Temps écoulé pour {} entree:".format(n), end - start)

seq = [4, 8, 2, 1, 23, 15]
insert_sort(seq)
print(seq)

get_time_algo("1_000")
get_time_algo("2_000")
get_time_algo("3_000")
get_time_algo("10_000")
