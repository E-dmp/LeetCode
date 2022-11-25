#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        iterator1 = list1
        iterator2 = list2
        dummyNode = ListNode()
        edge = dummyNode

        while iterator1 and iterator2:

            if iterator1.val < iterator2.val: 
                edge.next = iterator1
                iterator1 = iterator1.next
            else:
                 edge.next = iterator2
                 iterator2 = iterator2.next

            edge = edge.next

        if iterator1 is not None: edge.next = iterator1    
        if iterator2 is not None: edge.next = iterator2   
        
        return dummyNode.next 
        
# @lc code=end

