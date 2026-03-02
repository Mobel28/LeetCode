class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)

        swap = 0
        for i in range(n):
            req = n - 1 - i
            j = i
            while j < n and trailing[j] < req:
                j += 1

            if j == n:
                return -1
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swap += 1
                j -= 1

        return swap