class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        tempSet=set(nums)
        mul=k 
        while mul in tempSet:
            mul+=k
        return mul