class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=0
        for i in range(len(nums)):
            if nums[i]==nums[p]:
                continue
            else:
                p+=1
                nums[p]=nums[i]
        return p+1