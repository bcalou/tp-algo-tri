import random
import time

final_test = [random.randint(0, 100) for i in range(100)]

array2 = [0,1,2,6,1,0,15,12,3,8,9]

array3 = [77,75,72,70,60,52,41,3,2,21,21,10]

#fonction permmettant du fusionner 2 tableaux triés
#en un seul tableau triés
def merge(list1: list[int], list2: list[int]) -> list[int]:
    final_list: list[int] = []
    size_list1 = len(list1)
    size_list2 = len(list2)

    #tant que le tableau final est pas terminé
    #je compare les premiers élements des 2 tableaux
    #je prend le plus petit et le met dans le tableau final
    #j'enlève du tableau de base le nombre que je viens de prendre 
    #je recommence
    #une fois vide comme les tableaux sont déjà trié, je peux prendre
    #directement tout le contenu de celui qui reste
    while len(final_list) < size_list1 + size_list2:
        if list1 == []:
            final_list.extend(list2)
        elif list2 == []:
            final_list.extend(list1)
        elif list1[0] <= list2[0]:
            final_list.append(list1[0])
            list1.pop(0)
        else:
            final_list.append(list2[0])
            list2.pop(0)
    return final_list

#fonction final de tri
#elle permet de diviser le tableau donné en 2 jusqu'à avoir
#des tableaux à un élement déjà trié
def sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    middle_index: int = len(array)//2
    left_array: list[int] = sort(array[middle_index:])
    right_array: list[int] = sort(array[:middle_index])

    #retourne en les tableaux trié en partant de ceux à 1 élement
    #jusqu'à la taille du tableau initiale
    return merge(right_array, left_array)

start: float = time.time()

sort(final_test)

end: float = time.time()

print("Temps écoulé :", end - start)
