import random

random_list = random.sample(range(100), 10)

def selection_sort(random_list):
    list_len = len(random_list)
    for i in range(list_len):
        min_number = random_list[i]
        min_index = i
        for j in range(i, list_len):
            if min_number > random_list[j]:
                min_number = random_list[j]
                min_index = j
            print(str(min_number) + ":"+ str(min_index) +":"+ str(j))

        if min_index != i:
            temp = random_list[i]
            random_list[i] = random_list[min_index]
            random_list[min_index] = temp
        # print("Step:"+ str(i).zfill(2) + ": "+ str(random_list))

print("Step:"+ str(-1) + ": "+ str(random_list))
selection_sort(random_list=random_list)