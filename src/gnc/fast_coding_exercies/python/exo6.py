import time

def trouver_paire_calibration(releves, cible):
    #dictionnaire clé:nombre, valeur : index
    dict_complementary = {}
    for index,value in enumerate(releves):
        complement = cible-value
        if complement in dict_complementary:
            return (complement, value)
        dict_complementary[value]=index

    # Ton code ici. 
    # Indice : Utilise un set() pour mémoriser les valeurs déjà vues pendant que tu parcours la liste.
    pass


# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : Cas simple
    print(f"Test 1 : {trouver_paire_calibration([10, 15, 3, 7], 17)}") 
    # Attendu : (10, 7) ou (7, 10)

    # Test 2 : Aucun résultat
    print(f"Test 2 : {trouver_paire_calibration([1, 2, 3], 10)}") 
    # Attendu : None

    # Test 3 : Le piège du même index
    print(f"Test 3 : {trouver_paire_calibration([5, 2, 9], 10)}") 
    # Attendu : None (on ne peut pas utiliser le 5 deux fois)

    # Test 4 : Test de Performance (Simulation TestDome)
    print("Test de performance en cours (1 000 000 d'éléments)...")
    # On crée une liste de 1 million d'éléments [0, 1, 2, 3... 999997, 999998, 999999]
    gros_tableau = list(range(1000000)) 
    cible_complexe = 1999997 # Seule solution : 999998 + 999999
    
    debut = time.time()
    resultat = trouver_paire_calibration(gros_tableau, cible_complexe)
    fin = time.time()
    
    print(f"Résultat : {resultat}")
    print(f"Temps : {fin - debut:.4f} secondes")
    
    if (fin - debut) > 0.5:
        print("ÉCHEC : Timeout ! Ton algorithme est en O(n²).")
    else:
        print("SUCCÈS : Algorithme optimisé en O(n) !")