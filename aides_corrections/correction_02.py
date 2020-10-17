# Calculer la moyenne des éléments d'une liste

def moyenne(ma_liste:list)->float:
    """ Renvoie la moyenne d'une liste
        Précondition: ma-liste n'est pas vide
    """
    somme = 0
    for element in ma_liste:
        somme += element
    return somme / len(ma_liste)

assert moyenne([-1.5, 0.0, 1.5, 4.0]) == 1.0, 'Le test n\'est pas passé'
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
moyenne(L)
