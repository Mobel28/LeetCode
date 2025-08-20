class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma=0
        res=set()
        i=0
        for j in range(len(s)):
            while s[j]in res:
                res.remove(s[i])
                i+=1
            res.add(s[j])
            ma=max(len(res),ma)
        return ma