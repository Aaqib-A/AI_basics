import random

random_list = random.sample(range(100), 10)
random_list = [86, 1, 71, 66, 79, 57, 89, 2, 10, 18]

def insertion_sort (random_list):
    list_len = len(random_list)
    for i in range(1, list_len):
        key = random_list[i]
        j = i -1
        while j >=0 and key < random_list[j]:
            random_list[j+1] = random_list[j]
            j=j-1
        random_list[j+1] = key
        print("Step:"+ str(i).zfill(2) + ": "+ str(random_list))
"""
def insertion_sort (random_list):
    list_len = len(random_list)
    for i in range(1, list_len):
        key = random_list[i]
        print("key: "+str(key))
        for j in range (i-1, -1, -1):
            print(str(j) +":"+ str(random_list [j]))
            if key < random_list [j]:
                print(str(random_list [j]) +":"+ str(random_list [j+1]) +":"+str(random_list[i]))
                print(j+1)
                print(random_list[j+1])
                random_list[j+1] = random_list[j]
                print(random_list[j+1])
            else:
                print("ERROR")
                # random_list[j] = key
                random_list[j] = key
                break
            
        print(str(i), " :Hello", str(random_list[i]))
        print()

        random_list[i-1] = key

        print("Step:"+ str(i).zfill(2) + ": "+ str(random_list))
"""


print("Step:"+ str(-1) + ": "+ str(random_list))
insertion_sort(random_list=random_list)

