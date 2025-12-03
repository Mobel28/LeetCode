class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Better Solution
        count0=0
        count1=0
        count2=0
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        for i in range(0,count0):
            nums[i]=0
        for i in range(count0,count0+count1):
            nums[i]=1
        for i in range(count0+count1,len(nums)):
            nums[i]=2
        return nums
        #TC=O(2N)
        #SC=O(1)