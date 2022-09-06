# Find the first index of a matching number in the list

def find_first_index(arr, item, si=0):
    arr_len = len(arr)
    if si==arr_len:
        return -1
    if arr[si]==item:
        return si
    index = find_first_index(arr, item, si+1)
    return index

arr = [2, 5, 6, 7, 8, 3, 5, 7, 8, 8, 10, 3, 4]
item = 8
find_first_index(arr, item)



# Find the first index of a matching number in the list

def find_last_index(arr, item, last_ind):
    arr_len = len(arr)
    if last_ind==0:
        return -1
    if arr[last_ind]==item:
        return last_ind
    match_index = find_last_index(arr, item, last_ind-1)
    print(match_index)
    return match_index

arr = [2, 5, 6, 7, 8, 3, 5, 7, 8, 6, 10, 3, 4]
item = 6
find_last_index(arr, item, len(arr)-1)
