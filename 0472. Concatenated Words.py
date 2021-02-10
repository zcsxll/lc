from typing import List

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.root = Node()
        self.words = words
        for word in words:
            self.insert(word)

        ret = []
        for word in words:
            if self.check(word, 0, 0, [-1]*len(word)):
                ret.append(word)
        return ret

    def check(self, word, start_idx, cnt, mem):
        if start_idx >= len(word):
            return cnt >= 2
        if mem[start_idx] >= 0: #说明从start_idx开始往后的判断已经做过了
            return mem[start_idx] > 0

        node = self.root
        for i in range(start_idx, len(word)):
            n = ord(word[i]) - ord('a')
            node = node.child[n]
            if node is None:
                mem[start_idx] = 0
                return False
            
            if node.is_leaf:
                if self.check(word, i + 1, cnt + 1, mem):
                    mem[start_idx] = 1
                    return True
        return False

    def insert(self, word):
        node = self.root
        for w in word:
            n = ord(w) - ord('a')
            if node.child[n] is None:
                node.child[n] = Node()
            node = node.child[n]
        node.is_leaf = True

words = ["cat","dog","catdog"]
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# words = ["a","b","ab","abc"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
ret = Solution().findAllConcatenatedWordsInADict(words)
print(ret)
