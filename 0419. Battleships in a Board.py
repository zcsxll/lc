from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        self.H = len(board)
        if self.H <= 0:
            return 0
        self.W = len(board[0])
        self.flag = [[0] * self.W for _ in range(self.H)]
        self. ret = 0
        for y in range(self.H):
            for x in range(self.W):
                self.dfs(board, y, x)

        # print(flag)
        return self.ret

    def dfs(self, board, y, x):
        if self.flag[y][x] == 1:
            return
        self.flag[y][x] = 1
        if board[y][x] == '.':
            return
        
        if x > 0 and self.flag[y][x-1] == 0 and board[y][x-1] == 'X':
            self.dfs(board, y, x-1)
        elif x < self.W-1 and self.flag[y][x+1] == 0 and board[y][x+1] == 'X':
            self.dfs(board, y, x+1)
        elif y > 0 and self.flag[y-1][x] == 0 and  board[y-1][x] == 'X':
            self.dfs(board, y-1, x)
        elif y < self.H-1 and self.flag[y+1][x] == 0 and board[y+1][x] == 'X':
            self.dfs(board, y+1, x)
        else:
            # print(y, x)
            self.ret += 1

board = [
    ['X', '.', '.', 'X'],
    ['.', '.', '.', 'X'],
    ['.', '.', '.', 'X']
]
ret = Solution().countBattleships(board)
print(ret)