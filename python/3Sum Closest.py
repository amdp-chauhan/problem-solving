"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

# Solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        distance_from_target = float('inf')
        
        sorted_list = sorted(nums)
        
        for current in range(len(sorted_list)):
            left_point = current + 1
            right_point = len(sorted_list) - 1

            while left_point < right_point:
                new_sum = sorted_list[current] + sorted_list[left_point] + sorted_list[right_point]

                if abs(target - new_sum) < abs(distance_from_target):
                    distance_from_target = target - new_sum

                if distance_from_target == 0:
                    return new_sum

                if new_sum < target:
                    left_point += 1
                else:
                    right_point -= 1
            
        return target - distance_from_target
