from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        dp = [[0] * N for _ in range(M)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else -dungeon[-1][-1] + 1
        for y in range(M-2, -1, -1):
            dp[y][-1] = -dungeon[y][-1] + dp[y+1][-1]
            if dp[y][-1] < 1:
                dp[y][-1] = 1
        for x in range(N-2, -1, -1):
            dp[-1][x] = -dungeon[-1][x] + dp[-1][x+1]
            if dp[-1][x] < 1:
                dp[-1][x] = 1

        for y in range(M-2, -1, -1):
            for x in range(N-2, -1, -1):
                tmp = min(dp[y+1][x], dp[y][x+1])
                dp[y][x] = -dungeon[y][x] + tmp
                if dp[y][x] < 1:
                    dp[y][x] = 1

        return dp[0][0]

if __name__ == '__main__':
    dungeon = [[-2, -3, 3],
                [-5, -10, 1],
                [10, 30, -5]]
    # dungeon = [[0,0]]
    ret = Solution().calculateMinimumHP(dungeon)
    print(ret)
