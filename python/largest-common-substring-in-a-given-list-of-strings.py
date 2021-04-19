#### Longest common string
def longestCommonSubstring(strs) -> str:

    if len(strs) == 0:
        return ''

    result_substr = strs[0]

    # iterate over substrings (string from second)
    for item in strs[1:]:
        index = 0
        initial = result_substr
        temp_common = ''
        common = ''

        # iterate over characters:
        while len(initial)>index and len(item)>index:
            # compare elements on a given index
            if initial[index] == item[index]:
                temp_common += initial[index]
                # if new common is greater than previously obtained common
                if len(temp_common)>len(common):
                    common = temp_common
            else:
                # reset current common
                temp_common=''
            index+=1
        # set new common as best common substr so far
        result_substr = common
        
    return result_substr    

print(longestCommonSubstring(['amaaarr', 'amaaaradee', 'amaaarmdee']))
