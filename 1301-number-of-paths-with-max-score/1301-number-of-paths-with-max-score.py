from functools import lru_cache
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        @lru_cache(None)
        def solve(i, j):
            # Out of bounds
            if i < 0 or j < 0:
                return (-1, 0)

            # Obstacle
            if board[i][j] == 'X':
                return (-1, 0)

            # Reached E
            if i == 0 and j == 0:
                return (0, 1)

            # Three possible previous cells
            up_score, up_ways = solve(i - 1, j)
            left_score, left_ways = solve(i, j - 1)
            diag_score, diag_ways = solve(i - 1, j - 1)

            best = max(up_score, left_score, diag_score)

            # No path exists
            if best == -1:
                return (-1, 0)

            ways = 0

            if up_score == best:
                ways = (ways + up_ways) % MOD

            if left_score == best:
                ways = (ways + left_ways) % MOD

            if diag_score == best:
                ways = (ways + diag_ways) % MOD

            score = best

            # Add current cell value if it's a digit
            if board[i][j].isdigit():
                score += int(board[i][j])

            return (score, ways)

        score, ways = solve(n - 1, n - 1)

        if score == -1:
            return [0, 0]

        return [score, ways]