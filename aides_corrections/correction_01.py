# Liste sans tete

def sans_tete(ma_liste:list)->list:
    """ Renvoie une copie de ma_liste privée du premier élément
        Précondition ma_liste n'est pas vide.
        Postcondition: la taille de la liste renvoyée est plus petite d'un élément par rapport à ma_liste
    """
    # On initialise une liste vide
    liste_sortie = []
    # On ajoute à liste_sortie chaque élement de ma_liste en commençant du deuxième jusqu'au dernier
    for i in range(1,len(ma_liste)):
        liste_sortie.append(ma_liste[i])
    return liste_sortie

assert sans_tete([-1, 0, 1, 4]) == [0, 1, 4], 'Le test n\'est pas passé'
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
sans_tete(L)
