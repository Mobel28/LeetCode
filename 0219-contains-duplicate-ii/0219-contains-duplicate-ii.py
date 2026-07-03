class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp=dict()
        res=False
        for i,val in enumerate(nums):
            if val in temp and abs(temp[val]-i)<=k:
                res=True
                temp[val]=i
            else:
                temp[val]=i
        return res

