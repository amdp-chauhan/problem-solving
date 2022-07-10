"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Accepted
1,966,281
Submissions
6,101,527
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        polindrome = s[0] if len(s)>0 else ""
        processed={}
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r - l + 1 > len(polindrome):
                    polindrome = s[l:r+1]
                l-=1
                r+=1
            
            # even
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r - l + 1 > len(polindrome):
                    polindrome = s[l:r+1]
                l-=1
                r+=1
        
        return polindrome
