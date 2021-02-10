from typing import List
# import copy

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Node()
        self.words = words

        for word in words:
            self.insert_word(word)

        self.ret = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                node = self.root
                self.search(node, y, x, board)
                
                if len(self.ret) >= len(self.words):
                    break
            if len(self.ret) >= len(self.words):
                    break
        return self.ret

    def search(self, node, y, x, board):
        if board[y][x] == ' ':
            return

        # print(board[y][x])
        n = ord(board[y][x]) - ord('a')
        if node.child[n] is None:
            return
        node = node.child[n]
        if node.word is not None:
            self.ret.append(node.word)
            node.word = None
            if len(self.ret) >= len(self.words):
                return

        old = board[y][x]
        board[y][x] = ' '
        if y > 0:
            self.search(node, y-1, x, board)
        if x > 0:
            self.search(node, y, x-1, board)
        if y < len(board) - 1:
            self.search(node, y+1, x, board)
        if x < len(board[0]) - 1:
            self.search(node, y, x+1, board)
        board[y][x] = old

    def insert_word(self, word):
        node = self.root
        for w in word:
            n = ord(w) - ord('a')
            if node.child[n] is None:
                node.child[n] = Node()
            node = node.child[n]
        node.word = word

if __name__ == '__main__':
    board = [["a","b"],["c","d"]]
    words = ["abdc", "ab", "ad", "acd", "dbac"]

    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # words = []

    ret = Solution().findWords(board, words)
    print(ret)