class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return 0
        negative=(dividend<0)!=(divisor<0)
        dividend=abs(dividend)
        divisor=abs(divisor)   
        quotient=0 
        while dividend>=divisor:
            temp=divisor
            mul=1
            while dividend>=temp+temp:
                mul=mul+mul
                temp=temp+temp
            dividend=dividend-temp
            quotient+=mul
        if negative:
            quotient=-quotient
        if quotient>2**31-1:
            return 2**31-1
        if quotient<-2**31-1:
            return -2**31-1
        return quotient