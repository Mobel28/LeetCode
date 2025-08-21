class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits)==0:
            return []
        if len(digits)==1:
            char=letters[int(digits)]
            base=[]
            for ch in char:
                base.append(ch)
            return base 
        fic=digits[0]
        word=letters[int(fic)]
        temp=self.letterCombinations(digits[1:])
        ans=[]
        for c in word:
            for sub in temp:
                ans.append(c+sub)
        return ans