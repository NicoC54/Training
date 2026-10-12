


def filtre_et_inverse(liste):
    return [word[::-1] for word in liste if len(word)>=5]



def twosum(liste, target):

    vu = {}

    for index,number in enumerate(liste):
        complement = target - number

        if complement in vu.keys()
            return (vu[complement],index)
        
        vu[number] = index
        