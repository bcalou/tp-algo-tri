import time
import random


def sort(table: list[int]) -> list[int]:
    if len(table) <= 1:
        return table
    middle: int = len(table) // 2

    first_part: list[int] = table[:middle]
    second_part: list[int] = table[middle:]
    first_part = sort(first_part)
    second_part = sort(second_part)

    final_table: list[int] = []
    final_table = merge(final_table, first_part, second_part)

    return final_table


def merge(final_table: list[int], table1: list[int], table2: list[int]) -> list[int]:

    if (len(table1) == 0):
        return final_table + table2

    if (len(table2) == 0):
        return final_table + table1

    if table1[0] <= table2[0]:
        final_table.append(table1[0])
        table1.remove(table1[0])
        return merge(final_table, table1, table2)

    final_table.append(table2[0])
    table2.remove(table2[0])
    return merge(final_table, table1, table2)

array = [random.randint(0, 100) for i in range(100)]

print(sort(array))
