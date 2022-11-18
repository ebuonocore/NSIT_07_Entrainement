# Comparaison graphique entre deux tris

# Importe la bibliothèque time et matplotlib.plot
from pylab import *

def compare_les_tris_et_trace(N:int):
    """ Lance N fois le tri d'une liste de taille croissante selon 2 algorithmes
        Mémorise pour chaque taille t de la liste, les temps d'exécution
        Trace le graphique d'évolution des temps de tri en fonction de la taille t de la liste
    """
    # Initialise les listes pour mémoriser la taille de L, le temps de chaque algorithme
    tailles = []
    temps_tri_selection = []
    temps_tri_sorted = []

    for t in range (10, 200, 10):
        temps1, temps2 = compare_les_tris(N, t)

        tailles.append(t)
        temps_tri_selection.append(temps1)
        temps_tri_sorted.append(temps2)
    
    plot(tailles, temps_tri_selection, label="tri_selection()")
    plot(tailles, temps_tri_sorted, label="sorted()") 
    xlabel("Taille des listes")
    ylabel("Temps")
    legend()
    show()
    
compare_les_tris_et_trace(50)
