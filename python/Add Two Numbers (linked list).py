"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1, l2)
        num1 = f'{l1.val}'
        num2 = f'{l2.val}'
        while l1.next!=None:
            l1 = l1.next
            num1 = f'{l1.val}{num1}'
        while l2.next!=None:
            l2 = l2.next
            num2 = f'{l2.val}{num2}'
        # print(num1, num2)
        
        sum_of_nums = int(num1)+int(num2)
        result_nodes = point = ListNode(0)
        # print(f'{sum_of_nums}'[::-1])
        for num in f'{sum_of_nums}'[::-1]:
            point.next = ListNode(num)
            point = point.next
        # print(point, result_nodes)
        return result_nodes.next
