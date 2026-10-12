class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remMap={0:1}
        res=0
        prefixSum=0
        for i in nums:
            prefixSum+=i
            rem=prefixSum%k
            if rem in remMap:
                res+=remMap[rem]
            remMap[rem]=remMap.get(rem,0)+1
        return res