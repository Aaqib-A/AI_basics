import random

def random_sequence_generator(max,n):
    random_list = random.sample(range(max), n)
    return random_list

# print(random_sequence_generator(20,10))