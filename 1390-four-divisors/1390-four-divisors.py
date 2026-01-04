class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            dummy=[]
            j=1
            while j*j<=i:
                if i%j==0:
                    dummy.append(j)
                    if j!=i//j:
                        dummy.append(i//j)
                j+=1
            if len(dummy)==4:
                res+=sum(dummy)
        return res