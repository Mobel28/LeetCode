class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        maxProd=float(-inf)
        prefix=1
        suffix=1
        for i in range(n):
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            maxProd=max(maxProd,max(prefix,suffix))
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
        return maxProd