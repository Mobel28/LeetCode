# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        max_sum=float('-inf')
        level=1
        max_level=1
        while queue:
            curr_sum=0
            size=len(queue)
            for _ in range(size):
                curr_val=queue.popleft()
                curr_sum+=curr_val.val
                if curr_val.left:
                    queue.append(curr_val.left)
                if curr_val.right:
                    queue.append(curr_val.right)
            if curr_sum>max_sum:
                max_sum=curr_sum
                max_level=level
            level+=1
        return max_level