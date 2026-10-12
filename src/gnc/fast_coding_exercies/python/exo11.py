def nettoyer_telemetrie(paquets):

    liste_deplacee = []

    for value in paquets:
        if value == 0:
            continue
        else:
            liste_deplacee.append(value)
    
    longueur_deplacee = len(liste_deplacee)
    longueur_initiale = len(paquets)

    for i in range (longueur_deplacee, longueur_initiale):
        liste_deplacee.append(0)

    return liste_deplacee



# --- BLOC DE TESTS ---
if __name__ == "__main__":
    print(f"Test 1 : {nettoyer_telemetrie([0, 1, 0, 3, 12])}") 
    # Attendu : [1, 3, 12, 0, 0]

    print(f"Test 2 : {nettoyer_telemetrie([0, 0, 0])}") 
    # Attendu : [0, 0, 0]

    print(f"Test 3 : {nettoyer_telemetrie([4, 2, 8])}") 
    # Attendu : [4, 2, 8]