class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i%3==0:
                continue
            else:
                diff=3-i
                print((diff+i)//3)
                count+=(diff+i)//3
        return count