class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0 
        right=len(numbers)- 1
        while left<right:
            totalSum=numbers[left]+numbers[right]
            if totalSum==target:
                return left+1,right+1
            elif totalSum<target:
                left+=1
            else:
                right-=1