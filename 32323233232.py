import random
w = str(input('Введите слово:'))

e = 5
z=random.choices(w, k= e)
print("".join(z))