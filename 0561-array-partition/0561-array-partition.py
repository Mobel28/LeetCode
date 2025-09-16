class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        temp=sorted(nums)
        i=0
        m=0
        while i<len(nums):
            m+=temp[i]
            i+=2
        return m