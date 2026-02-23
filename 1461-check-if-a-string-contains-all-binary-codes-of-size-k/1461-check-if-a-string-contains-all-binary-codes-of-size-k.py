class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        seen = set()
        num = 0   
        for i in range(n):
            num = ((num << 1) & ((1 << k) - 1)) | int(s[i])         
            if i >= k - 1:
                seen.add(num)
        
        return len(seen) == (1 << k)