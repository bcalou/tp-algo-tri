def factoriel(i):
    if(i > 0):
        return i * factoriel(i-1)
    else:
        return 1


print(factoriel(5))

