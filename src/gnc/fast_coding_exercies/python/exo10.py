def pic_de_signal(signaux, k):

    if len(signaux) < k:
        return None

    somme_max = 0

    for i in range(k):
        somme_max += signaux[i]

    somme = somme_max
    index_depart = 0

    for i in range (k, len(signaux)):
        
        somme -= signaux[index_depart]
        somme += signaux[i]

        index_depart +=1

        if  (somme > somme_max) :
            somme_max = somme

    return somme_max




# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : Cas classique
    # Les blocs de 3 sont : [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
    # Le max est 9
    print(f"Test 1 : {pic_de_signal([2, 1, 5, 1, 3, 2], 3)}") 
    # Attendu : 9

    # Test 2 : Fenêtre très large
    print(f"Test 2 : {pic_de_signal([1, 9, -1, -2, 7, 3, -1, 2], 4)}") 
    # Attendu : 13 (qui correspond à [9, -1, -2, 7])

    # Test 3 : Le Edge Case (Tableau trop petit)
    print(f"Test 3 : {pic_de_signal([5, 2], 3)}") 
    # Attendu : 0 ou None