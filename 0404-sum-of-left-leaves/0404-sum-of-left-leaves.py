# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if not root:
                return 0
            s=0
            if root.left and not root.left.left and not root.left.right:
                s += root.left.val
            s += fun(root.left)
            s += fun(root.right)
            return s
        return fun(root)  