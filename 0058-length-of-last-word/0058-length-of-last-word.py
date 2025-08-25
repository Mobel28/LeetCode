class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li=s.split()
        return(len(li[-1]))