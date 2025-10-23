class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def ffind(nums,tar):
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=l+(r-l)//2
                if nums[m]==tar:
                    res=m
                    r=m-1
                elif nums[m]<=tar:
                    l=m+1
                else:
                    r=m-1
            return res
        def lfind(nums,tar):
            l=0
            r=len(nums)-1
            res=-1
            while l<=r:
                m=l+(r-l)//2
                if nums[m]==tar:
                    res=m
                    l=m+1
                elif nums[m]<tar:
                    l=m+1
                else:
                    r=m-1
            return res
        return [ffind(nums,target),lfind(nums,target)]