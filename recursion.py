import random

array = [random.randint(0, 100) for i in range(10)]

def factorial(n : int) :
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

print(factorial(4))

def merge(gauche,droite):
    res=[]
    igauche = 0 #index de gauche
    idroite = 0 #index de droite
    while igauche < len(gauche) and idroite < len(droite):
        if gauche[igauche] <= droite[idroite]:
            res.append(gauche[igauche])
            igauche = igauche + 1
        else:
            res.append(droite[idroite])
            idroite = idroite + 1
    if gauche:
        res.extend(gauche[igauche:])
    if droite:
        res.extend(droite[idroite:])
    return res

def sort(tab):
    if len(tab) > 1:
        milieu = len(tab) //2
        gauche= tab[:milieu]
        droite= tab[milieu:]
        gauche = sort(gauche)
        droite = sort(droite)
        res = merge(gauche,droite)
    else:
        res = tab
    return res

print(array)
print(sort(array))