class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax=[-1 for _ in range(len(height))]
        rightMax=[-1 for _  in range(len(height))]
        leftMax[0]=height[0]
        rightMax[-1]=height[-1]
        i=1
        j=len(height)-2
        while i<len(height) and j>=0:
            leftMax[i]=max(leftMax[i-1],height[i])
            rightMax[j]=max(rightMax[j+1],height[j])
            i+=1
            j-=1
        res=0
        for i in range(len(height)):
            if height[i]<leftMax[i] and height[i]<rightMax[i]:
                res+=min(leftMax[i],rightMax[i])-height[i]
        return res
        # return 0