class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefSum = [0] * (n + 1)
        prefCnt = [0] * (n + 1)
        prefConc = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)
            prefSum[i + 1] = prefSum[i] + d
            prefCnt[i + 1] = prefCnt[i]
            prefConc[i + 1] = prefConc[i]

            if d:
                prefCnt[i + 1] += 1
                prefConc[i + 1] = (prefConc[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            sm = prefSum[r + 1] - prefSum[l]
            cnt = prefCnt[r + 1] - prefCnt[l]

            num = (
                prefConc[r + 1]
                - prefConc[l] * pow10[cnt]
            ) % MOD

            ans.append(num * sm % MOD)

        return ans