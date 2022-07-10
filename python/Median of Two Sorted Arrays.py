"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        main_list = nums1+nums2
        arr_length = len(main_list)
        if (len(nums1)>0 and len(nums2)>0 and nums2[0]<nums1[-1]):
            for i in range(1, arr_length):
                for j in range (i, 0, -1):
                    if main_list[j]<main_list[j-1]:
                        main_list[j-1], main_list[j] = main_list[j], main_list[j-1]
 
        if (len(main_list)%2 is not 0):
            return main_list[int((arr_length+1)/2)-1]

        first_item = int(arr_length/2)
        return (main_list[first_item-1]+main_list[first_item])/2
