class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="AEIOUaeiou"
        i=0
        j=len(s)-1
        temp=list(s)
        while i<j:
            if temp[i] in vowels and temp[j] in vowels:
                temp[i],temp[j]=temp[j],temp[i]
                i+=1
                j-=1
                continue
            if temp[i] not in vowels:
                i+=1
            if temp[j] not in vowels:
                j-=1
        return "".join(temp)