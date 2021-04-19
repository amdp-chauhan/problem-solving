def merge_two_sorted_list(a, b):
    sorted_list = []
    i = 0 # for list a
    j = 0 # for list b

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i<len(a):
        sorted_list.append(a[i])
        i+=1

    while j<len(b):
        sorted_list.append(b[j])
        j+=1

    return sorted_list

def merge_sort(listt):
    if len(listt)<=1:
        return listt
    mid = (len(listt))//2
    list1 = divide_list(listt[:mid])
    list2 = divide_list(listt[mid:])
    sorted_list = merge_two_sorted_list(list1, list2)
    return sorted_list

print(merge_sort([1, 3, 2, 5, 4, 7, 6, 8, 11, 9, 10]))
