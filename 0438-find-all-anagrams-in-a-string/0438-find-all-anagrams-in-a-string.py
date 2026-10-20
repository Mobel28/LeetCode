class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        smap={}
        pmap={}
        for i in p:
            pmap[i]=pmap.get(i,0)+1
        l=0
        count=len(p)
        res=[]
        for r in range(len(s)):
            smap[s[r]]=smap.get(s[r],0)+1
            if s[r] in pmap and pmap[s[r]]>=smap[s[r]]:
                count-=1
            if r-l+1>len(p):
                smap[s[l]]-=1
                if s[l] in pmap and smap[s[l]]<pmap[s[l]]:
                    count+=1
                l+=1
            if count==0:
                res.append(l)
        return res
                