class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq=Counter(digits)
        count=0
        for h in range(1,10):
            for t in range(10):
                for u in range(0,10,2):
                    if h==t==u:
                        if freq[h]>=3:
                            count+=1
                    elif h==t:
                        if freq[h]>=2 and freq[u]>=1:
                            count+=1
                    elif h==u:
                        if freq[h]>=2 and freq[t]>=1:
                            count+=1
                    elif t==u:
                        if freq[t]>=2 and freq[h]>=1:
                            count+=1
                    else:
                        if freq[h]>=1 and freq[t]>=1 and freq[u]>=1:
                            count+=1
            
        return count



            
