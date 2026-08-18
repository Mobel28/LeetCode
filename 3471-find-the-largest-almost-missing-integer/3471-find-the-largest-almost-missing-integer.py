class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
            count={}
            for i in range(len(nums)-k+1):
                for num in set(nums[i:i+k]):
                    count[num]=count.get(num,0)+1
            return max((num for num in count if count[num]==1), default=-1)