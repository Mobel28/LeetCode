# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def counter(root):
            if root:
                left=counter(root.left)
                right=counter(root.right)
                return 1+max(left,right)
            else:
                return 0
        return counter(root)                
