class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[v]=nums[i]
                v+=1
        return v