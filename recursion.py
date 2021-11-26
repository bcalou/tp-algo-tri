def factorielle(number: int) -> int:
    resultat: int = number * factorielle(number - 1) 
    return  resultat