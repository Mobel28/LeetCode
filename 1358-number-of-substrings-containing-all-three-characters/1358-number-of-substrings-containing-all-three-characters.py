class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res=0
        n=len(s)
        freq={'a':0,'b':0,'c':0}
        left=0
        for right in range(len(s)):
            freq[s[right]]+=1
            while freq['a'] and freq['b'] and freq['c']:
                res+=n-right
                freq[s[left]]-=1
                left+=1

        return res
#TC=O(N)
#SC=O(1)