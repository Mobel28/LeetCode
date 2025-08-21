import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d={}
        ban=set(banned)
        word=re.findall(r'\w+',paragraph.lower())
        for i in word:
            if i not in ban:
                d[i]=d.get(i,0)+1
        return max(d,key=d.get)