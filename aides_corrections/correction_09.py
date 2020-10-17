# Trouve le maximum d'une liste en récursif

def maximum_rec(ma_liste:list, m:float)->float:
    """ Renvoie le maximum de la liste ma_liste
        Précondition: ma_liste n'est pas vide.
    """
    # Cas de base: Si la taille de ma_liste = 1, alors, renvoit le maximum entre l'élément restant et m
    if len(ma_liste)==1:
        return max(ma_liste[0], m)
    # Sinon, renvoit maximul_rec(ma_liste privée de la tête, maximum entre la tête de la liste et m)
    else:
        nouveau_max = max(ma_liste[0],m)
        ma_liste_sans_tete = sans_tete(ma_liste) # Copie la liste privée du premier élément
        return maximum_rec(ma_liste_sans_tete,nouveau_max)

L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
assert maximum_rec([1,2,5,3],0)==5, 'La fonction maximum ne renvoie pas le bon résultat sur une liste d\'entiers'
assert maximum_rec([1.8,2.4,5.1,3.1],0)==5.1, 'La fonction maximum ne renvoie pas le bon résultat sur une liste de flottants'
maximum_rec(L,L[0])
