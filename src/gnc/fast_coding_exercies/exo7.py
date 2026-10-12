def find_equilibrium_index(masses):
    somme_totale = 0
    somme_gauche = 0

    for i in range (len(masses)):
        somme_totale += masses[i]

    for i in range (len(masses)):
        
        if somme gauche == somme_totale - masses[i] - somme_gauche:
            return i

        somme_gauche += masses[i]

    return -1

    

   
        