# Trouver le maximum de la liste

def maximum(ma_liste:list)->float:
    """ Renvoie le maximum de la liste ma_liste
        Précondition: ma_liste n'est pas vide
    """
    m = ma_liste[0] # Initialise la maximum au premier élément de la liste
    for element in ma_liste:
        if element > m:
            m = element
    return m

assert maximum([1,2,5,3])==5, 'La fonction maximum ne renvoie pas le bon résultat sur une liste d\'entiers'
assert maximum([1.8,2.4,5.1,3.1])==5.1, 'La fonction maximum ne renvoie pas le bon résultat sur une liste de flottants'
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
maximum(L)
