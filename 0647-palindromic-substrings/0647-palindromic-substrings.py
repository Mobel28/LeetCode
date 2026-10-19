class Solution:
    def countSubstrings(self, s: str) -> int:
        def pal(s,l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        count=0
        for i in range(len(s)):
            count+=pal(s,i,i)
            count+=pal(s,i,i+1)
        return count
