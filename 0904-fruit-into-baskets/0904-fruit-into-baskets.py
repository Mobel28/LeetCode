class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        tempMap={}
        res=0
        l=0
        for r in range(len(fruits)):
            tempMap[fruits[r]]=tempMap.get(fruits[r],0)+1
            while len(tempMap)>2:
                tempMap[fruits[l]]-=1
                if tempMap[fruits[l]]==0:
                    del tempMap[fruits[l]]
                l+=1
            
            res=max(r-l+1,res)
        return res