class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def firstidx():
            l,r=0,len(nums)-1
            res=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    res=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return res
        def lastidx():
            l,r=0,len(nums)-1
            res=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    l=mid+1
                    res=mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return res
        return [firstidx(),lastidx()]