class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma=0
        for i in range(len(s)):
            res=s[i]
            for j in range(i+1,len(s)):
                if s[j]in res:
                    break
                else:
                    res+=s[j]
            ma=max(len(res),ma)
        return ma