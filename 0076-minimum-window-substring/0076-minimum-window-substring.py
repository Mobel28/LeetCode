class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # i=0
        # j=0
        # res=""
        # while j<len(t) and i<len(s):
        #     res+=s[i]

        #     if s[i]==t[j]:
        #         j+=1
        #     i+=1
        need={}
        for i in t:
            need[i]=need.get(i,0)+1
        left=0
        formed=0
        req=len(need)
        start=0
        window={}
        minVal=float('inf')
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            if s[right] in need and window[s[right]]==need[s[right]]:
                formed+=1
            while formed==req:
                    if (right-left)+1<minVal:
                        minVal=(right-left)+1
                        start=left
                    if s[left] in need and need[s[left]]==window[s[left]]:
                        formed-=1
                    window[s[left]]-=1
                    left+=1
    
        return "" if minVal==float('inf') else s[start:start+minVal]