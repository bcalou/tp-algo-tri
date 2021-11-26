import time
import random

def merge(first_table: list[int], second_table: list[int]) -> list:
    partially_sorted_table : list[int] = []
    i = j = 0
    #boucle while qui permet de comparer les 2 tableau d'entrées entre eux et de trier les valeurs dans un nouveau tableau
    while i < len(first_table) and j < len(second_table):
        if first_table[i] < second_table[j] :
            partially_sorted_table.append(first_table[i])
            i += 1
        else :
            partially_sorted_table.append(second_table[j])
            j += 1   
    #Pour ajouter les valeur manquants on passe par 2 extend (boucle if plus optimizer ?)   
    partially_sorted_table.extend(first_table[i:])
    partially_sorted_table.extend(second_table[j:])
    return partially_sorted_table

def sort(table: list[int]) -> list[int]:
    table_length = len(table)
    #On arrête la récursivité quand le tableau vaut 1 (parce qu'il est techniquement trié)
    if table_length <= 1:
        return table 

    split = table_length // 2
    #On découpe le tableau en 2 de manière récursive.
    return merge(sort(table[:split]), sort(table[split:]))
    

table = [random.randint(0, 100) for i in range(10)]

start: float = time.time()
sort(table)
end: float = time.time()
print("Temps écoulé :", end - start)