class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq1=[0 for _ in range(26)]
        for i in s1:
            freq1[ord(i)-ord('a')]+=1
        freq2=[0 for _ in range(26)]
        l=0
        for r in range(len(s2)):
            freq2[ord(s2[r])-ord('a')]+=1
            if r-l+1>len(s1):
                freq2[ord(s2[l])-ord('a')]-=1
                l+=1
            if freq1==freq2:
                return True
        return False