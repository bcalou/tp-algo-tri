def factorielle(valeur : int) :
    if valeur == 0 or valeur == 1 :
        return 1
    else :
        return valeur * factorielle(valeur -1)

print(factorielle(5))