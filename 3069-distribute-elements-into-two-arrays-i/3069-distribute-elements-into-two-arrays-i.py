class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        for i in nums[2:]:
            if arr1[-1]>arr2[-1]:
                arr1.append(i)
            else:
                arr2.append(i)
        return list(arr1+arr2)