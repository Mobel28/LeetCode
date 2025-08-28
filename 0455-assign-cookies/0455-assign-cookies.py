class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c_idx=0
        c_count=0
        while c_idx<len(s) and c_count<len(g):
            if s[c_idx]>=g[c_count]:
                c_count+=1
            c_idx+=1
        return c_count