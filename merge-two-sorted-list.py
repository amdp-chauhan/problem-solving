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

list1 = [1, 4, 5, 7, 11]
list2 = [2, 6, 8, 9, 12, 13, 20]
print(merge_two_sorted_list(list1, list2))
