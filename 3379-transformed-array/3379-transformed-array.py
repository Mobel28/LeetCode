class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            if nums[i]>0:
                step=nums[i]+i
                step=step%n
                print(step)
                res[i]=nums[step]
            elif nums[i]<0:
                step=(i-abs(nums[i]))%n
                res[i]=nums[step]
            else:
                res[i]=nums[i]
        return res