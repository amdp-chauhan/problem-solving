"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

# Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) < 1:
            return ""

        common_prefix = ""    
        shortest_str_len = min([len(a) for a in strs])
        # print('shortest_str_len',shortest_str_len)
        
        # at max common prefix will be of the length of smalles string in a given list
        for i in range(shortest_str_len, 0, -1):
            # start from the assumption that for a given lenth all item prefix are common
            is_common = True
            # first string for comparison
            prev_str = strs[0][:i]
            # iterate over each string in a given list
            for j_str in strs[1:]:
                # if next string contains any other prefix for lenth i, then no need to proceed further, just break the loop and check for lenth i-1
                if prev_str != j_str[:i]:
                    is_common = False
                    break

            # If is_common is True, means for a given length 'i', we have got a common prefix
            if is_common:
                # Since we are iterating from max common length to 0, so no need to iterate any further, because obtained common prefix is already best.
                common_prefix = prev_str
                break

        return common_prefix
                
