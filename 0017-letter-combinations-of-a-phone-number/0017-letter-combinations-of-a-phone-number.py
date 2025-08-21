class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits)==0:
            return []
        sol=[]
        def kpc(digits,ans):
            if len(digits)==0:
                sol.append(ans)
                return
            word=letters[int(digits[0])]
            for ch in word:
                kpc(digits[1:],ans+ch)
        kpc(digits,"")
        return sol