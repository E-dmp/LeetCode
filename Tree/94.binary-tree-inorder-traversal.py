#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        return self.inorderTraversalHelper(root, [])


    def inorderTraversalHelper(self,root,arr):

        if root == None : return None

        self.inorderTraversalHelper(root.left, arr)
        arr.append(root.val)
        self.inorderTraversalHelper(root.right,arr)

        return arr
        
# @lc code=end

