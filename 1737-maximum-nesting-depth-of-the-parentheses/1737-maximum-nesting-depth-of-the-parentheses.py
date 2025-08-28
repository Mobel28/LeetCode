class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxcount=0
        for i in s:
            if i in {'(',')'}:
                if i=='(':
                    count+=1 
                    maxcount=max(maxcount,count)
                elif i==')':
                    count-=1                 
        return maxcount