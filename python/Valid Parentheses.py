"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for element in s:
            if element in '({[':
                stack.append(element)
            elif len(stack)==0:
                return False
            elif closing_dict[stack.pop()]!=element:
                return False

        return len(stack) == 0
                  
                
