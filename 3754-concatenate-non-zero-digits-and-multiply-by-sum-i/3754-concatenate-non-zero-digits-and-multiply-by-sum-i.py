class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nonZero=0
        place=1
        sumVal=0
        while n>0:
            cDigit=n%10
            if cDigit!=0:
                nonZero+=cDigit*place
                sumVal+=cDigit
                place*=10
            n//=10
        return nonZero*sumVal