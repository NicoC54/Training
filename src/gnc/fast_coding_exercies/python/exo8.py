def premier_paquet_unique(paquets):
    # Ton code optimisé ici en O(n)

    dico = {}
    for value in paquets:
        if value in dico.keys():
            dict[value]+=1
        else dict[value]=1

    for value,number in dico.items():
        if dict[value]==1:
            return value


    return None


# --- BLOC DE TESTS ---
if __name__ == "__main__":
    # Test 1 : Cas classique
    print(f"Test 1 : {premier_paquet_unique([4, 5, 1, 2, 0, 4, 1, 2])}") 
    # Attendu : 5 (4 est répété, 5 est unique et arrive en premier)

    # Test 2 : Aucun unique
    print(f"Test 2 : {premier_paquet_unique([9, 9, 8, 8])}") 
    # Attendu : None

    # Test 3 : Le dernier est l'unique
    print(f"Test 3 : {premier_paquet_unique([7, 7, 3, 3, 2])}") 
    # Attendu : 2