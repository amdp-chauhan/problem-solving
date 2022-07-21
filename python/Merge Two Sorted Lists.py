"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_list = [list1.val] if list1 else []
        list2_list = [list2.val] if list2 else []
        if len(list1_list)>0:
            while list1.next:
                list1 = list1.next
                if list1.val!=None:
                    list1_list.append(list1.val)
        if len(list2_list)>0:
            while list2.next:
                list2 = list2.next
                if list2.val!=None:
                    list2_list.append(list2.val)

        sorted_list = sorted(list1_list+list2_list)
        # print(list1_list, list2_list, sorted_list)
        result = node = ListNode(0)
        for item in sorted_list:
            node.next = ListNode(item)
            node = node.next

        return result.next
