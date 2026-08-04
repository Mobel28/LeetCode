class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet=[-1 for _ in range(256)]
        l=0
        r=0
        n=len(s)
        res=0
        while r<n:
            if hashSet[ord(s[r])]!=-1:
                if l<=hashSet[ord(s[r])]:
                    l=hashSet[ord(s[r])]+1
            res=max(res,(r-l)+1)
            hashSet[ord(s[r])]=r
            r+=1
        return res