class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum=0
        tempMap={}
        l=0
        temp=0
        for r in range(len(nums)):
            while nums[r] in tempMap:
                del tempMap[nums[l]]
                temp-=nums[l]
                l+=1
            temp+=nums[r]
            tempMap[nums[r]]=1
            if len(tempMap)==k:
                maxSum=max(maxSum,temp)
                del tempMap[nums[l]]
                temp-=nums[l]
                l+=1
        return maxSum

            