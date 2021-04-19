def sort_alphabets(text):
    # using function
    print('Auto-sort:',''.join(sorted(text)))

    # custom logic
    # using Merge sort
    print('Merge-sort:',''.join(merge_sort(text)))

    # using Bubble sort
    compy_text = list(text)
    for i in range(0, len(compy_text)):
        for j in range(0, len(compy_text)-i-1):
            if compy_text[j]>compy_text[j+1]:
               compy_text[j], compy_text[j+1] = compy_text[j+1], compy_text[j] 

    print('Bubble-sort:',''.join(compy_text))

print(sort_alphabets('asdfajskkfjasdhfk'))
