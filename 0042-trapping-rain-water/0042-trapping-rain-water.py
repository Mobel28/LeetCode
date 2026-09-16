class Solution:
    def trap(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        leftMax=-1
        rightMax=-1
        total=0
        while l<r:
            if height[l]<=height[r]:
                if height[l]<leftMax:
                    total+=leftMax-height[l]
                else:
                    leftMax=height[l]
                l+=1
            else:
                if height[r]<rightMax:
                    total+=rightMax-height[r]
                else:
                    rightMax=height[r]
                r-=1
        return total