class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations=0
        while True:
            is_sorted=True
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    is_sorted=False
                    break
            if is_sorted:
                return operations
            min_sum=float('inf')
            min_idx=-1
            for i in range(1,len(nums)):
                curr_sum=nums[i]+nums[i-1]
                if curr_sum<min_sum:
                    min_sum=curr_sum
                    min_idx=i-1
            new_nums=[]
            for i in range(min_idx):
                new_nums.append(nums[i])
            new_nums.append(min_sum)
            for i in range(min_idx+2,len(nums)):
                new_nums.append(nums[i])
            operations+=1
            nums=new_nums