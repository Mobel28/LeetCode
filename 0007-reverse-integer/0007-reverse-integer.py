class Solution:
    def reverse(self, x: int) -> int:
        y=0
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            pop=x%10
            x//=10
            if y > (2**31 - 1) // 10 or (y == (2**31 - 1) // 10 and pop > 7):
                return 0
            y=y*10+pop
        y=y*sign
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y