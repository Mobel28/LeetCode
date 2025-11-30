class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot=sum(nums)
        tar=tot%p
        if tar==0:
            return 0
        mp={0:-1}
        pre=0
        res=len(nums)
        for i,x in enumerate(nums):
            pre=(pre+x)%p
            need=(pre-tar+p)%p
            if need in mp:
                res=min(res,i-mp[need])
            mp[pre]=i
        return -1 if res==len(nums) else res