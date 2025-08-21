class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if  k==1:
            return 0
        b=self.kthGrammar(n-1,(k+1)//2)
        if k%2==1:
            return b
        else:
            b=1-b
            return b