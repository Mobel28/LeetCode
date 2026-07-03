class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=set()
        for i in nums:
            if i in temp:
                return True
            temp.add(i)
        return False