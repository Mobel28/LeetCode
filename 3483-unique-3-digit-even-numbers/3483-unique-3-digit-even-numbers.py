class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq=Counter(digits)
        count=0
        for i in  range(100,1000):
            if i%2!=0:
                continue
            tempfreq=Counter(str(i))
            for j in tempfreq.keys():
                    if freq[int(j)]<tempfreq[j]:
                        break
            else:
                count+=1
        return count



            
