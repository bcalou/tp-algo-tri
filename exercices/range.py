import time
import random as rd
from typing import List


def get_avg_exe_time_for(func, arg_func,batch_size=10, avg_size = 10) -> float:
    """func is the tested function and arg_func is a function that return func arguments"""
    avg: float = 0
    for i in range(avg_size):
        start : float = time.time()
        func(arg_func(batch_size))
        end : float = time.time()
        avg += end - start
    avg = round(avg / 10, 4)
    return avg


def generate_randint_list(size : int) -> list[int]:
    list : List[int] = [rd.randint(0,100) for i in range(size)]
    return list
        