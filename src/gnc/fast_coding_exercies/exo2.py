


def filtre_et_inverse(liste):

    words = liste.size()

    for word in liste:

        if (len(word)<5) :
            break

        else:
            liste2=[]
            liste2.append(word[::-1])
    
    return liste2

        