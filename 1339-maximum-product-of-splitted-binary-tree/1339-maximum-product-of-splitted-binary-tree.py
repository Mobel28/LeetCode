# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD=10**9+7
        self.maxval=0
        def totalsum(node):
            if not node:
                return 0
            total=node.val+totalsum(node.right)+totalsum(node.left)
            return total
        total=totalsum(root)
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            subsum=node.val+left+right
            self.maxval=max(self.maxval,subsum*(total-subsum))
            return subsum
        dfs(root)
        return self.maxval%MOD