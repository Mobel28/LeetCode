class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        rem=0
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0 or rem>0:
            r=rem
            if i>=0:
                r+=int(a[i])
                i-=1
            if j>=0:
                r+=int(b[j])
                j-=1
            res+=str(r%2)
            rem=r//2
        return res[::-1]

