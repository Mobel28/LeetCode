class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fnum=float('-inf')
        snum=float('-inf')
        tnum=float('-inf')
        for i in range(len(nums)):
            if nums[i]!=fnum and nums[i]!=snum and nums[i]!=tnum:
                if nums[i]>fnum:
                    tnum=snum
                    snum=fnum
                    fnum=nums[i]
                elif nums[i]>snum:
                    tnum=snum
                    snum=nums[i]
                elif nums[i]>tnum:
                    tnum=nums[i]
        print(fnum,snum,tnum)
        if tnum!=float('-inf'):
            return tnum 
        else:
             return fnum