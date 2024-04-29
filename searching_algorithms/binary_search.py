import math

ordered_list = [0,1,2,3,4,5,6,7,8,9]

def binary_search(target, start, end):
    print(start, end)
    if start > end:
        return "Not Found"
    
    middle = math.floor((start+end) / 2)
    if ordered_list[middle] == target:
        return "Found it at index: "+ str(middle)
    
    if ordered_list[middle]>target:
        return binary_search(target, start, middle-1)
    if ordered_list[middle]<target:
        return binary_search(target, middle+1, end)
    

output = binary_search(3, 0, len(ordered_list))
print(output)