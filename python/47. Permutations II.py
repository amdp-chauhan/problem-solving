'''

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def get_permutations(listt, left, right):
            if left==right:
                # print(listt)
                if not listt in permutations: permutations.append(listt.copy())

            for i in range(left, right):
                listt[left], listt[i] = listt[i], listt[left]
                get_permutations(listt, left+1, right)
                listt[left], listt[i] = listt[i], listt[left]

        get_permutations(nums, 0, len(nums))
        # print(permutations)
        return permutations
