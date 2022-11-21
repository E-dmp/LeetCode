#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        this solution is accepted but not clean code...
        """
        
        iterator = head
        arr = []

        # walk ListNode
        while iterator is not None:

            if iterator.val not in arr:
                arr.append(iterator.val)
            iterator = iterator.next

        length = len(arr)

        if length == 0: return head
        elif length == 1 : length += 1

        # create newNodeList
        newNodehead = ListNode(arr[0])
        currentNode = newNodehead

        for i in range(1,len(arr)):
            node = ListNode(arr[i])
            currentNode.next = node
            currentNode = node

        return newNodehead
        
# @lc code=end

