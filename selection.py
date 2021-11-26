import time
import random

def tri_selection(table: list) -> list:
    smallest_number: int = 0
    smallest_number_index: int = 0
    table_length: int = len(table)

    #Boucle imbriqué où l'on parcours le tableau dans chaque boucle (on ne reviens pas sur les index deja parcours sur la boucle imbriqué).
    for number in range(table_length):
        for compared_number in range(number,table_length):
            #On cherche le nombre le plus petit du tableau et le permute avec le nombre de l'index de la boucle externe où l'on ce trouve.
            if smallest_number > table[compared_number]:
                smallest_number = table[compared_number]
                smallest_number_index = compared_number
        table[number], table[smallest_number_index] = table[smallest_number_index], table[number]
    return table


table = [random.randint(0, 100) for i in range(30000)]

start: float = time.time()
tri_selection(table)
end: float = time.time()
print("Temps écoulé :", end - start)
