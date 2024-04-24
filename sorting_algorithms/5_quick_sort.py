import random
import math

# random_list = random.sample(range(100), 10)
random_list = [86, 1, 71, 66, 79, 57, 89, 2, 10, 18]

def quick_sort(random_list: list, low:int, high:int):
    if low < high:
        pivot_location = partition(random_list, low, high)
        quick_sort(random_list, low, pivot_location)
        quick_sort(random_list, pivot_location + 1, high)

    return random_list

def partition(data_list:list, low:int, high:int):
    pivot = data_list[low]
    left_wall = low

    for i in range(low+1, high):
        if data_list[i]<pivot:

            # Swap
            temp = data_list[i]
            data_list[i] = data_list[left_wall]
            data_list[left_wall] = temp
            left_wall = left_wall + 1

    # Swap
    temp = pivot
    pivot = data_list[left_wall]
    data_list[left_wall] = temp

    print("Pivot: " + str(pivot))
    print(data_list)
    print()

    return left_wall


print(random_list)
output = quick_sort(random_list, 0, len(random_list))
print(output)


