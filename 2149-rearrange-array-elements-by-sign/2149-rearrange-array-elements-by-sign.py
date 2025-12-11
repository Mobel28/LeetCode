class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        res=[0]*len(nums)
        for i in range((len(nums)//2)):
            res[i*2]=pos[i]
            res[(i*2)+1]=neg[i]
        return res
        #TC=O(n)
        #SC=O(n)