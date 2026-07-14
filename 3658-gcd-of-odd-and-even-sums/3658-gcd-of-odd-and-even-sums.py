class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(even,odd):
            if odd==0:
                return even
            return gcd(odd,even%odd)
    
        return gcd(n*(n+1),n*n)
                