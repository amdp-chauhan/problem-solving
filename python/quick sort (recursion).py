# Quick Sort - Merge sort was not really doing much, it was just recursively dividing & merging the list, through function calls. On the other hand, quick sort, performs the first operation on it's own, that is, finding the first pivot element position, then performs the recursive calls to perform the similar operation on left and right partitions.
def partition(arr, start, end):
    pivot_pos = start # init the point at the available start of array
    pivot_elem = arr[start]
    l = start
    while l<=end:
        if arr[l]<pivot_elem:
            pivot_pos += 1
        l += 1
    # print('pivot_pos',pivot_pos)
    arr[pivot_pos], arr[start] = arr[start], arr[pivot_pos]
    i = start
    j = end
    while i<j:
        if arr[i]<pivot_elem: # i is at the right position
            i += 1
        elif arr[j]>=pivot_elem: # j is at the right position
            j -= 1
        else: #Swapping needed 
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return pivot_pos

def quickSort(arr, start, end):
    # Please add your code here
    if start>=end:
        return

    pivot = partition(arr, start, end) # partition for the first pivot
    quickSort(arr, start, pivot-1) # iteratively perform the above partition for left part of the pivot
    quickSort(arr, pivot+1, end) # iteratively perform the above partition for right part of the pivot

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)
