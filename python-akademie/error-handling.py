# nacitani dat
def nacitani_txt():
    data = []

    file = open('numbers.txt', 'r')

    for radek in file.readlines():
        data.append(radek.strip('\n'))
        
    file.close()
    
    

nacitani_txt()