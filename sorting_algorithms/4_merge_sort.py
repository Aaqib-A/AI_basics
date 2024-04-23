import random
import math

# random_list = random.sample(range(100), 10)
random_list = [86, 1, 71, 66, 79, 57, 89, 2, 10, 18]

def merge_sort (random_list:list):
    list_len = len(random_list)
    if ( list_len <= 1 ):
        return random_list#[0]
    
    array_one = random_list[0:math.ceil(list_len/2)]
    array_two = random_list[math.ceil(list_len/2):list_len]

    # print(math.ceil(list_len/2))
    # print("array_one"+ str(array_one))
    # print("array_two"+ str(array_two))

    array_one = merge_sort(array_one)
    array_two = merge_sort(array_two)

    return merge(array_one, array_two)

def merge(array_one:list, array_two:list):

    array_merged = []

    while ( len(array_one)!=0 and len(array_two)!=0 ):
        if array_one[0] > array_two[0]:
            array_merged.extend([array_two[0]])
            array_two.pop(0)
        else:
            array_merged.extend([array_one[0]])
            array_one.pop(0)

    while len(array_one) != 0 :
        array_merged.extend([array_one[0]])
        array_one.pop(0)

    while len(array_two) != 0 :
        array_merged.extend([array_two[0]])
        array_two.pop(0)

    print("array_merged" + str(array_merged))

    return array_merged

print(random_list)
output = merge_sort(random_list)
print(output)