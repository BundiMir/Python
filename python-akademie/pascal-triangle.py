def vytvoreni_hodnot(pocet_radku):
    """Tato funkce vrati seznam seznamu s nasimi hodnotami."""
    troj = []
    for radek in range(pocet_radku):
        troj.append([])

        for bunka in range(radek + 1):
            if bunka == 0 or bunka == len(troj[radek - 1]):
                troj[radek].append(1)
            else:
                predch_krok = troj[radek - 1]
                troj[radek].append(predch_krok[bunka] + predch_krok[bunka - 1])
    # print(troj)
    return troj

def vykreslit(troj):
    '''Tato funkce vykresli hodnoty z funkce vytvoreni_hodnot'''
    del_nejdelsiho_radku = 0

    if len(troj[0]) > len(troj[-1]):
        i = 0
    else:
        i = -1

    for symbol in troj[i]:
        del_nejdelsiho_radku += len(str(symbol))
    
    for radek in troj:
        for pozice, cislo in enumerate(radek):
            radek[pozice] = str(cislo)
        print(' '.join(radek).center(del_nejdelsiho_radku + len(troj) -1))
        
vykreslit(vytvoreni_hodnot(5))