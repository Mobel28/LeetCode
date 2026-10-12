class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums[:])
        # print(total)
        leftSum=0
        for i in range(len(nums)):
            rightSum=total-nums[i]-leftSum
            if leftSum==rightSum:
                return i
            leftSum+=nums[i]
        return -1
