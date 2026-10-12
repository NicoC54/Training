def max_gain_energie(niveaux):

    valid_min = niveaux[0]
    ecart_max = 0

    for value in niveaux :
        if value < valid_min :
            valid_min = value
        else:
            ecart = value - valid_min
            if ecart > ecart_max:
                ecart_max = ecart

    return ecart_max

# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : On commence à 1 (index 1), on relâche à 6 (index 4). Gain = 6 - 1 = 5.
    print(f"Test 1 : {max_gain_energie([7, 1, 5, 3, 6, 4])}") 
    # Attendu : 5

    # Test 2 : Chute libre continue, aucun gain possible.
    print(f"Test 2 : {max_gain_energie([7, 6, 4, 3, 1])}") 
    # Attendu : 0
    
    # Test 3 : Tableau vide ou trop petit.
    print(f"Test 3 : {max_gain_energie([5])}") 
    # Attendu : 0