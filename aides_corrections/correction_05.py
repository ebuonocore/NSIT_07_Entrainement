# Tri par sélection

def tri_selection(ma_liste:list)->list:
    """ Renvoie une copie triée dans m'ordre croissant de ma_liste
        Précondion: ma_liste n'est pas vide
        Post_condition: liste_triee a le même nombre d'éléments que ma_liste
    """
    # On initialise la liste_triee vide
    liste_triee = []
    # On copie la liste d'origine pour ne pas la détériorer
    ma_liste_copie = ma_liste.copy() # Evite les effets de bord
    # Tant qu'il reste un élément dans ma_liste_copie
    while len(ma_liste_copie)>0:
        # On trouve le maximum et sa position dans ma_liste grâce à maximum_position()
        maxi, position = maximum_position(ma_liste_copie)
        # Ajoute ce maximum à liste_triee
        liste_triee.append(maxi)
        # Retire ce maximum à ma_liste_copie
        del ma_liste_copie[position]
    return liste_triee

assert tri_selection([3,5,1,2]) == [5,3,2,1], 'Le test n\'est pas passé'
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
tri_selection(L)
