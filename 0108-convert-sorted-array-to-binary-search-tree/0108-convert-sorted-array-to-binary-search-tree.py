# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bin(n):
            if not n:
                return None
            mid=len(n)//2
            root=TreeNode(n[mid])
            root.left=bin(n[0:mid])
            root.right=bin(n[mid+1:])
            return root
        return bin(nums)

