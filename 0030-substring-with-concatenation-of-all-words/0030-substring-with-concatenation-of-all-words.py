class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s)<len(words)*len(words[0]):
            return []
        wordLen=len(words[0])
        totalWords=len(words)
        wordsMap=Counter(words)
        res=[]
        for offset in range(wordLen):
            left=offset
            count=0
            currMap={}
            for right in range(offset,len(s)-wordLen+1,wordLen):
                word=s[right:right+wordLen]
                if word not in wordsMap:
                    currMap.clear()
                    count=0
                    left=right+wordLen
                    continue
                currMap[word]=currMap.get(word,0)+1
                count+=1
                while currMap[word]>wordsMap[word]:
                    leftword=s[left:left+wordLen]
                    currMap[leftword]-=1
                    count-=1
                    left+=wordLen
                if count==totalWords:
                    res.append(left)
                    leftword=s[left:left+wordLen]
                    currMap[leftword]-=1
                    count-=1
                    left+=wordLen
        return res