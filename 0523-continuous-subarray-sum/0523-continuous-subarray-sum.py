class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        PrefMap={0:-1}
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            rem=curr%k
            if rem in PrefMap:
                if i-PrefMap[rem]>=2:
                    return True
            else:
                PrefMap[rem]=i
            # print(PrefMap)
        return False