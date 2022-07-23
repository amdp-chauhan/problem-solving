
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""

class Solution:
    def permute(self, nums):
        
        result = []
        
        if len(nums)==1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.pop(0) # pop the first item and hold it in a variable

            # find the permutation of remaining items
            combinations = self.permute(nums)
            
            # Iterate over each permutation, and add the popped item at last
            for comb in combinations:
                comb.append(n)

            # add newly formed combinations in the result list
            result.extend(combinations)
            
            # add the popped item back to the list at the last position
            nums.append(n)

        return result
