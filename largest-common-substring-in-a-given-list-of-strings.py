class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final_common = ''
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        initial = strs[0]
        for item in strs[1:]:
            index = 0
            common = ''
            final_common = ''
            while len(initial)>index and len(item)>index:
                #print(index, initial,len(initial), item,len(item))
                if initial[index] == item[index]:
                    common += initial[index]
                    if len(common)>len(final_common):
                        final_common = common
                        #print(final_common)
                else:
                    common=''
                index+=1
            initial = final_common
        return final_common       
