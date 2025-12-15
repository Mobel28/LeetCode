class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        pos=0
        neg=1
        for i in range(len(nums)):
            if nums[i]<0:
                res[neg]=nums[i]
                neg+=2
            else:
                res[pos]=nums[i]
                pos+=2
        return res
    #TC=O(n)
    #SC=O(n)