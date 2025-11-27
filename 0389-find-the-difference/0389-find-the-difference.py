class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ords=sum(ord(x) for x in s)
        ordt=sum(ord(x) for x in t)
        return chr(ordt-ords)
