"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for c in s:
            if not c in  list(s_dict.keys()): s_dict[c] = 1
            else: s_dict[c] += 1
        for c in t:
            if c in list(s_dict.keys()) and s_dict[c]>0: s_dict[c] -= 1
            else: return False
        return sum(list(s_dict.values()))==0
