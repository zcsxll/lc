from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.m = len(matrix)
        if self.m <= 0:
            return []
        self.n = len(matrix[0])
        self.flag = [[0] * self.n for _ in range(self.m)]
        for x in range(self.n):
            self.dfs(matrix, x, 0, 1)
        for y in range(self.m):
            self.dfs(matrix, 0, y, 1)

        self.ret = []

        for x in range(self.n):
            self.dfs(matrix, x, self.m-1, 2)
        for y in range(self.m):
            self.dfs(matrix, self.n-1, y, 2)

        # for line in self.flag:
            # print(line)
        return self.ret

    def dfs(self, matrix, x, y, k):
        if k == 2 and self.flag[y][x] == 1:
            # print(x, y)
            self.ret.append([y, x])
        if self.flag[y][x] == k:
            return
        self.flag[y][x] = k
        h = matrix[y][x]
        if x > 0 and h <= matrix[y][x-1]:
            self.dfs(matrix, x-1, y, k)
        if x < self.n-1 and h <= matrix[y][x+1]:
            self.dfs(matrix, x+1, y, k)
        if y > 0 and h <= matrix[y-1][x]:
            self.dfs(matrix, x, y-1, k)
        if y < self.m-1 and h <= matrix[y+1][x]:
            self.dfs(matrix, x, y+1, k)

if __name__ == '__main__':
    matrix = [
        [1,  2,   2,  3,  5],
        [3,  2,   3,  4,  4],
        [2,  4,   5,  3,  1],
        [6,  7,   1,  4,  5],
        [5,  1,   1,  2,  4]]
    matrix = [
        [1, 1],
        [1, 1],
        [1, 1]]
    ret = Solution().pacificAtlantic(matrix)
    print(ret)