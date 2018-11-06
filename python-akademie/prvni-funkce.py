
# def is_title(seznam):
#     for w in seznam:
#         if w.istitle():
#             return True
#         else:
#             return False

# seznam = ['Petr', 'Marek', 'Honza']
# result = is_title(seznam)
# print(result)

# def soucet(start,stop):
#     result = 0
#     for number in range(start,stop):
#         result += number
#     return result
# result = soucet(1,5)
# print(result)

# print('This is the first line\tThis is the second line')

# def soucet(start,stop):
#     result = 0
#     for number in range(start,stop):
#         result += number
#     return result

# result = soucet(1,10)
# print(result)

# def greet():
#     print('Hello')

# def to_kilograms(weight):
#     return weight * 0.45

# def to_meters(height):
#     return height * 0.025
    
# def bmi(weight, height):
#     return to_kilograms(weight) / to_meters(height) **2

# print(bmi(125, 63))

import random

# random = random.random() *200

# print(random)

# lst = [1,2,3,4,5,6,7,8,9,10]

# random.shuffle(lst)
# print(lst)

# words = ['jana','petr','dusan','karel']
# word = random.choice(words)
# print(word)
# guess = input('Guess the word: ')
# result = 'guessed' if guess == word else 'not guessed'
# # if guess == word:
# #     result = 'guessed'
# # else:
# #     result = 'not guessed'
# print(result)

# def add_three(a):
#     suma = a + 3
#     return suma
    
# result = add_three(5)
# print(result)

# def all_title(items):

#     for item in items:
    
#         if not item.istitle():
#             return False
            
#     print('Bye')
#     return True

# result = all_title('LL')
# print(result)



def min(sequence):
    minval = sequence[0]
    for item in sequence[1:]:
        if item < minval:
            minval = item
    return minval

lst = [8,2,3,1,4,5,6]
result = min(lst)
print(result)


# def my_min(sequence):
#     min = sequence[0]
#     for item in sequence[1:]:
#         if item < min:
#             min = item
#     return min


# lst = [8,2,3,1,4,5,6]
# result = my_min(lst)
# print(result)




