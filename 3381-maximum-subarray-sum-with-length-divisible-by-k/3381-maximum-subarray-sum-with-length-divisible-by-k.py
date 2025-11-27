class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        inf = 10**18
        ans = -inf

        sub = [inf] * k
        sub[0] = 0
        pre = 0

        for i in range(1, n + 1):
            pre += nums[i - 1]
            rem = i % k

            if sub[rem] != inf:
                ans = max(ans, pre - sub[rem])

            sub[rem] = min(sub[rem], pre)

        return ans
