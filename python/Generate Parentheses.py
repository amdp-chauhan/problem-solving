"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        def generate(combination, open_count, close_count):
            # print(combination, open_count, close_count)
            
            # stop the recursive call if we have reached the boundary
            if open_count>n or close_count>n or open_count<close_count:
                return
            
            # If both opening and closing parenthesis have reached their limit
            if open_count==n and close_count==n:
                combinations.append(combination)
                
            # If their is still an space for opening parenthesis
            if open_count < n:
                generate(combination+'(', open_count+1, close_count)
                generate(combination+')', open_count, close_count+1)
            else:
                generate(combination+')', open_count, close_count+1)
                
        # We know that first will always be the opening parenthesis
        generate('(', 1, 0)
        
        print(f'result: {combinations}')
        return combinations
