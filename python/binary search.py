# Binary Search
def binary_search(arr, item, left, right):
    if left > right:
        return -1
    
    middle = (left + right)//2

    if arr[middle]==item:
        return middle
    elif arr[middle]>item:
        return binary_search(arr, item, left, middle-1)
    else:
        return binary_search(arr, item, middle+1, right)

arr = [1, 3, 5, 6, 7, 9, 10, 12]
item = 12
binary_search(arr, item, 0, len(arr)-1)
