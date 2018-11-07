import random

dataset = [['Name','Item','Amount','Unit_Price', 'Total_Price']]

customers = ['Bettison, Elnora',
            'Doro, Jeffrey',
            'Idalia, Craig',
            'Conyard, Phil',
            'Skupinski, Wilbert',
            'McShee, Glenn',
            'Pate, Ashley',
            'Woodison, Annie']

products = [('DROXIA', 33.86),('WRINKLESS PLUS',23.55),
            ('Claravis', 9.85), ('Nadolol', 12.35),
            ('Quinapril', 34.89), ('Doxycycline Hyclate', 23.43),
            ('Metolazone', 43.06), ('PAXIL', 14.78)]

def datagen(rows):
    for i in range(rows):
        Name = random.choice(customers)
        Item, Unit_Price = random.choice(products)
        Amount = random.randint(1,100)
        Total_Price = Unit_Price * Amount

        row = [Name,Item,Amount,Unit_Price,Total_Price]
        dataset.append(row)
    return dataset

result = datagen(10)
print(result)