#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowPointer = head
        fastPointer = head

        while fastPointer is not None:

            if fastPointer.next != None:
                fastPointer = fastPointer.next.next
            else: 
                return False    

            slowPointer = slowPointer.next

            if fastPointer == slowPointer:
                return True

        return False
        
# @lc code=end

