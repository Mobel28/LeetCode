class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        temp=s.replace('-','').upper()
        count=0
        res=""
        for ch in reversed(temp):
            if count==k:
                res+='-'
                count=0
            res+=ch
            count+=1
        return "".join(reversed(res))