"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest_len = 0
        longest_str, temp_counter = '', 0
        for char in list(s):

            if char in longest_str:
                keep_substr = ""
                for sub_char in list(longest_str)[::-1]:
                    if char == sub_char:
                        break
                    keep_substr = sub_char+keep_substr

                longest_str, temp_counter = keep_substr, len(keep_substr)

            longest_str += char
            temp_counter+=1

            if temp_counter > largest_len:
                largest_len = temp_counter

        return largest_len

# Solution 2
class Solution:
    def lengthOfLongestSubstring(self, s: str, max_length: int = 0) -> int:
        if s:
            unique_string = ""
            for char in s:
                if char in unique_string:
                    break
                unique_string += char
            if len(unique_string) > max_length:
                max_length = len(unique_string)
            return self.lengthOfLongestSubstring(s[1:], max_length)
        return max_length
