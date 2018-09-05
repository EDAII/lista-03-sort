import random

one_million = 1000000

def populate(array):
    for i in range(len(array)):
        array[i] = random.randint(0, one_million)
    return array
