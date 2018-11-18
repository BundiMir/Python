def pocet_dni(datum1, datum2):
    if datum1 > datum2:
        datum1, datum2 = datum2, datum1
    
    pocet_dni = 0

    while datum1 < datum2:
        datum1 = pricitani (datum1)
        pocet_dni += 1
    
    print(pocet_dni)
    return pocet_dni

def pricitani(datum):
    # Pricitam dny:
        # dny v mesici
        # konce mesicu
            # kratke/dlouhe mes
            # unor
        # konec roku
    # 2019, 1, 1
    rok, mesic, den = datum
    



def prestupny_rok(y):
    return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))


print(pocet_dni((2017, 1, 1), (2017, 3, 1)))
