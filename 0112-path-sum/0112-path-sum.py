# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def help(root,target):
            if not root:
                return False
            if not root.left and not root.right and target==root.val:
                return True
            return (help(root.left,target-root.val) or help(root.right,target-root.val))
        return help(root,targetSum)