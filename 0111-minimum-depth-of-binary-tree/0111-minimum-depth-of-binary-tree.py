# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if root:
                left=fun(root.left)
                right=fun(root.right)
                if  left==0:
                    return right+1
                elif right==0:
                    return left+1
                else:
                    return 1+min(left,right)
            else:
                return 0
        return fun(root)