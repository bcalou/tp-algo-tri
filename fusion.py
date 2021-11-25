import time
import random


def sort_fusion(seq: list[int]) -> list[int]:
    # we divide the sequence into two equal parts
    # we traite each part
    if len(seq) <= 1:
        return seq
    mid = int(len(seq)/2) 
    seq_left = sort_fusion(seq[:mid])
    seq_right = sort_fusion(seq[mid:])
    return merge(seq_left, seq_right)


def merge(seq_left: list[int], seq_right: list[int]) -> list[int]:
    result = []
    i = 0  
    j = 0
    # compare the group of two elements eachtime and put the less one in the list result[]
    while i < len(seq_left) and j < len(seq_right):
        if seq_left[i] <= seq_right[j]:
            result.append(seq_left[i])
            i += 1
        else:
            result.append(seq_right[j])
            j += 1
    result += seq_left[i:]
    result += seq_right[j:]
    return result


def get_time_algo(n: str):
    a = int(n)
    array: list = [random.randint(0, 100) for _ in range(a)]
    start: float = time.time()
    sort_fusion(array)
    end: float = time.time()
    print("Temps écoulé pour {} entree:".format(n), end - start)


seq = [5, 3, 0, 6, 1, 4]
result = sort_fusion(seq)
print (result)

get_time_algo("1_000")
get_time_algo("2_000")
get_time_algo("3_000")
get_time_algo("10_000")
