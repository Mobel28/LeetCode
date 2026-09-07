class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
    
        while left<right:
            sumVal=numbers[left]+numbers[right]
            if sumVal==target:
                return [left+1,right+1]
            elif sumVal<target:
                left+=1
            else:
                right-=1
        
            
