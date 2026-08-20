class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        left=0
        right=len(height)-1
        # print(height[left],height[right])
        while left<right:
            h=min(height[left],height[right])
            a=right-left
            res=max(res,h*a)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res