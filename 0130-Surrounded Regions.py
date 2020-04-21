from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if board == []:
            return

        for i in range(len(board[0])):
            if board[0][i] == "O":
                self.handle1(board, 0, i)
            if board[len(board)-1][i] == "O":
                self.handle1(board, len(board) - 1, i)

        for i in range(len(board)):
            if board[i][0] == "O":
                self.handle1(board, i, 0)
            if board[i][len(board[0])-1] == "O":
                self.handle1(board, i, len(board[0])-1)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "-":
                    board[y][x] = "O"
                elif board[y][x] == "O":
                    board[y][x] = "X"

    def handle1(self, board, y, x):
        if len(board[0]) > x >= 0 and len(board) > y >= 0 and board[y][x] == "O":
            board[y][x] = "-"
            self.handle1(board, y-1, x)
            self.handle1(board, y, x-1)
            self.handle1(board, y+1, x)
            self.handle1(board, y, x+1)
        
if __name__ == "__main__":
    board = []
    board += [list("XXXX")]
    board += [list("XOOX")]
    board += [list("XXOX")]
    board += [list("XOXX")]
    for line in board:
        for p in line:
            print(p, end = "")
        print()

    Solution().solve(board)

    for line in board:
        for p in line:
            print(p, end = "")
        print()
    # print(board)