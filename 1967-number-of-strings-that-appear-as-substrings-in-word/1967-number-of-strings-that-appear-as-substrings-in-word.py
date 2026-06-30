class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        for cWord in patterns:
            found=False
            for start in range(len(word)):
                if found:
                    break
                for end in range(start+1,len(word)+1):
                    if word[start:end]==cWord:
                        count+=1
                        found=True
                        break
        return count
#TC=O(N^3)
#SC=O(1)