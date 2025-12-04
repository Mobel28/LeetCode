class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        return i,j
        # TC=O(N^2)
        # SC=O(1)