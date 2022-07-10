"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def sorting(lst):
            for i in range(len(lst),0,-1):
                for j in range(0, i-1):
                    if lst[j]>lst[j+1]:
                        lst[j], lst[j+1] = lst[j+1], lst[j]
            return lst 
        def get_values(linknode, response):
            response.append(linknode.val)
            if linknode.next == None:
                return response
            return get_values(linknode.next, response)
        
        list_nodes_sorted = point = ListNode(0)
        
        if len(lists)==0:
            return list_nodes_sorted.next
        # lists=[[]]
        # for item in lists:
        #     print(type(item), item)
        simple_lists = [get_values(item,[]) if item!=None else [] for item in lists]
        # print('simple_lists',simple_lists)
        complete_list = []
        for sub_list in simple_lists:
            complete_list = complete_list+sub_list
        sorted_list = sorted(complete_list)
        # print('final sorted list',sorted_list)
    
        for x in sorted_list:
            point.next = ListNode(x)
            point = point.next
        print(list_nodes_sorted.next)
        return list_nodes_sorted.next
