class Solution:
    def minWindow(self, s: str, t: str) -> str:
        req={}
        for i in t:
            req[i]=req.get(i,0)+1
        l=0
        window={}
        formed=0
        start=0
        minVal=float('inf')
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in req and window[s[r]]==req[s[r]]:
                formed+=1
            while formed==len(req):
                if r-l+1<minVal:
                    minVal=r-l+1
                    start=l
                if s[l] in req and req[s[l]]==window[s[l]]:
                    formed-=1
                window[s[l]]-=1
                l+=1
        return "" if minVal==float(inf) else s[start:start+minVal]

