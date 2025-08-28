class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        d={}
        for i in nums2:
            while stack and i>stack[-1]:
                d[stack.pop()]=i
            stack.append(i)
        while stack:
            d[stack.pop()]=-1
        print(d)
        for i in nums1:
            stack.append(d.get(i))
        return stack