import random
import string
from random import randint


def generate_random_name(number_of_names):
    for i in range(number_of_names):
        letters = string.ascii_letters
        my_str1 = ''.join(random.choice(letters) for j in range(randint(1, 15)))
        my_str2 = ''.join(random.choice(letters) for k in range(randint(1, 15)))
        yield (f'{my_str1} {my_str2}')


gen = generate_random_name(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

