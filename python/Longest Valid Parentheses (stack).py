"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""


		
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0
        match_index = [False] * len(s)
        stack = []
        paranthesis = [''] * len(s)
        longest_valid_match_count = 0
        for i in range(len(s)):
            if s[i]==')' and len(stack)>0:
                pop_index = stack.pop()
                if paranthesis[pop_index] == '(':
                    match_index[pop_index] = True
                    match_index[i] = True
            else:
                stack.append(i)
                paranthesis[i] = s[i]

        match_count = 0
        for match_flag in match_index:
            if match_flag: 
                match_count += 1
            else:
                match_count = 0
            
            longest_valid_match_count = max(longest_valid_match_count, match_count)

        return longest_valid_match_count
