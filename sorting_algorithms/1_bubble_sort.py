import random

random_list = random.sample(range(100), 10)

def bubble_sort(random_list:list):
    array_len = len(random_list)
    for i in range(array_len):
        for j in range(i, array_len):
            if random_list[i] < random_list[j]:
                temp = random_list[i]
                random_list[i] = random_list[j]
                random_list[j] = temp

        print("Step:"+ str(i).zfill(2) + ": "+ str(random_list))

print("Step:"+ str(-1) + ": "+ str(random_list))
bubble_sort(random_list=random_list)