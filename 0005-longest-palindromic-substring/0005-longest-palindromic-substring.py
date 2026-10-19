class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        strt,end=0,0
        for i in range(len(s)):
            len1=pal(s,i,i)
            len2=pal(s,i,i+1)
            maxLen=max(len1,len2)
            if maxLen>end-strt:
                strt=i-(maxLen-1)//2
                end=i+maxLen//2
        # print(strt,end)
        return s[strt:end+1]