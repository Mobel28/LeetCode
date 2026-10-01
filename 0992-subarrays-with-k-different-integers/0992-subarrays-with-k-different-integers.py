class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def localFunc(nums,k):
            l=0
            countMap={}
            res=0
            for r in range(len(nums)):
                countMap[nums[r]]=countMap.get(nums[r],0)+1
                while len(countMap)>k:
        
                    countMap[nums[l]]=countMap[nums[l]]-1
                    if countMap[nums[l]]==0:
                        del countMap[nums[l]]
                    l+=1
                res+=r-l+1
            return res
        return localFunc(nums,k)-localFunc(nums,k-1)