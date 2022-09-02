'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = 'asdfe'
        is_matching = False
        def get_permutations(listt, left, right):
            if left == right:
                # if ''.join(listt) in s2: is_matching = True
                return ''.join(listt) in s2

            for i in range(left, right):
                listt[left], listt[i] = listt[i], listt[left]
                t = get_permutations(listt, left+1, right)
                # print('t',t)
                if t: return t
                listt[left], listt[i] = listt[i], listt[left]

        is_matching = get_permutations(list(s1), 0, len(s1))
        # print(f'is_matching:{is_matching}')
        return is_matching

        
