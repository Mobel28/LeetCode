class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            temp = i
            while temp % 5 == 0:
                ans += 1
                temp = temp // 5
        return ans