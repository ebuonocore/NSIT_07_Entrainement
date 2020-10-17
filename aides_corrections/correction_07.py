# Compare les performances de deux tris

def compare_les_tris(N:int, taille:int)->tuple:
    """ Créé une liste de 'taille' éléments
        Chronomètre l'exécution de N tris du tri sélection et du tri par sorted()
        Renvoie le couple constitué des deux temps
    """
    # Importe la bibliothèque time
    import time
    # Créé une liste aléatoire de 'taille' éléments
    L = [randint(1,100) for i in range(1,taille)]

    # Relève le chronomètre
    temps_debut1 = time.time()
    # Boucle N fois le tri_selection L
    for i in range(N):
        tri_selection(L)
    # Relève le chronomètre
    temps_fin1 = time.time()
    temps1 = temps_fin1 - temps_debut1

    # Relève le chronomètre
    temps_debut2 = time.time()
    # Boucle N fois le tri_selection L
    for i in range(N):
        sorted(L)
    # Relève le chronomètre
    temps_fin2 = time.time()
    temps2 = temps_fin2 - temps_debut2
    
    return (temps1, temps2)

t1, t2 = compare_les_tris(10000, 50)
print("Sur une liste de 50 éléments")
print("Temps pris par 10000 répétitions de tri_selection():",t1)
print("Temps pris par 10000 répétitions de sorted():",t2)
