def max_poussee_continue(fluctuations):
    if not fluctuations:
        return 0

    score_en_cours = fluctuations[0]
    record_absolu = fluctuations[0]

    for valeur in fluctuations[1:]:

        score_en_cours = max(valeur, score_en_cours+valeur)

        if score_en_cours > record_absolu:
            record_absolu = score_en_cours

    return record_absolu

 





    # Ton code O(n) ici
    pass


# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : La meilleure séquence continue est [4, -1, 2, 1] dont la somme est 6.
    print(f"Test 1 : {max_poussee_continue([-2, 1, -3, 4, -1, 2, 1, -5, 4])}") 
    # Attendu : 6

    # Test 2 : S'il n'y a que du positif, on prend tout.
    print(f"Test 2 : {max_poussee_continue([1, 2, 3, 4, 5])}") 
    # Attendu : 15

    # Test 3 : S'il n'y a que du négatif, on prend le "moins pire" (le max).
    print(f"Test 3 : {max_poussee_continue([-5, -2, -9])}") 
    # Attendu : -2