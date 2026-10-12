def premier_signal_unique(flux):
    dico_redondance = {}

    if flux == "":
        return -1

    for letter in flux :
        if letter in dico_redondance.keys():
            dico_redondance[letter]+=1
        else:
            dico_redondance[letter]=1

    for index,letter in enumerate(flux) :
        if dico_redondance[letter]==1:
            return index

    return -1

