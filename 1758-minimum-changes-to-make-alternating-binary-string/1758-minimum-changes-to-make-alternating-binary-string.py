class Solution:
    def minOperations(self, s: str) -> int:
        change_strt_0=0
        change_strt_1=0
        for i,ch in enumerate(s):
            if ch!=('0' if i%2==0 else '1'):
                change_strt_0+=1
            if ch!=('1' if i%2==0 else '0'):
                change_strt_1+=1
        return min(change_strt_0,change_strt_1)
