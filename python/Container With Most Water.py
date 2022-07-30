"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
    ## Approach 1
        # max_height = 0
        # heights = []
        # for i in range(len(height)):
        #     for j in range(len(height)-1, i, -1):
        #         new_height = (j-i)*min(height[i],height[j])
        #         print(i,j,'::',new_height)
        #         if new_height > max_height:
        #             max_height = new_height
        # return max_height
    ## Approach 2
        max_height = 0
        left, right = 0, len(height)-1
        while left<right:
            new_height = (right-left) * min(height[left],height[right])
            # print(left, right, new_height)
            max_height = new_height if new_height > max_height else max_height
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_height
