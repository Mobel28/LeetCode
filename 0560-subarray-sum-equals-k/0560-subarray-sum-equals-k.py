class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefMap={}
        prefMap[0]=1
        prefSum=0
        res=0
        for i in nums:
            prefSum+=i
            if prefSum-k in prefMap:
                res+=prefMap[prefSum-k]
            prefMap[prefSum]=prefMap.get(prefSum,0)+1
        return res