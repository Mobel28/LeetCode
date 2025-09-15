class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        for i in text.split():
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count+=1
        return count