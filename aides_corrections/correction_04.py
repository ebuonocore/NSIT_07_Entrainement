# Trouver le maximum de la liste n°2: Renvoie le maximum et son indice

def maximum_position(ma_liste:list)->tuple:
    """ Renvoie le maximum de la liste ma_liste et son indice
        Précondition: ma_liste n'est pas vide
    """
    pos = 0 # Initalise la position du maximum à m'indice 0 (premier élément de la liste)
    m = ma_liste[0] # Initialise la maximum au premier élément de la liste
    for i in range(len(ma_liste)):
        if ma_liste[i] > m:
            pos = i
            m = ma_liste[i]
    return m,pos

assert maximum_position([1,2,5,3])==(5, 2), 'La fonction maximum ne renvoie pas le bon résultat sur une liste d\'entiers'
assert maximum_position([1.8,2.4,5.1,3.1])==(5.1, 2), 'La fonction maximum ne renvoie pas le bon résultat sur une liste de flottants'
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
maximum_position(L)
