# Trouver les deux extrêmes de la liste (plus petit et plus grand éléments) 

# On peut s'aider de la fonction tri_selection() vu précédemment
def extremum(ma_liste:list)->tuple:
    """ Renvoie l'élément le plus petit et le plus grand sous la forme du p-uplet (minimum, maximum)
        Précondition: ma_liste contient au moins deux éléments
        
    :param list ma_liste: Liste à examiner.

    :return: Le couple constitué de (minimum, maximum)
    
    >>> extremum([3,5,1,2])
    (1, 5)
    
    >>> extremum([-1,-3,7,5,3,2])
    (-3, 7)
    
    >>> extremum([3.2,5.1,1.6,-2.2])
    (-2.2, 5.1)
    
    >>> extremum(['A','R','Z'])
    ('A', 'Z')
    """
    assert len(ma_liste) >= 2, 'La liste doit contenir au moins 2 éléments'
    ma_liste_copie = tri_selection(ma_liste.copy())
    maximum = ma_liste_copie[0]
    minimum = ma_liste_copie[-1]
    return (minimum, maximum)

import doctest
doctest.testmod(verbose=True) 
L = [randint(1,100) for i in range(1,20)] # Tire une liste aléatoire
print(L)
extremum(L)
