from typing import List

class Node:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.root = Node()
        for word in dictionary:
            self.insert(word)

        i = 0
        ret = ''
        while i < len(sentence):
            i_, w = self.search(sentence[i:])
            # print(i, w)
            ret += w + ' '
            if i_ < 0:
                break
            i += i_
        return ret[:-1]

    def insert(self, word):
        node = self.root
        for w in word:
            off = ord(w) - ord('a')
            if node.child[off] is None:
                node.child[off] = Node()
            node = node.child[off]
            if node.is_leaf: #已经存在比word短的root，因此word不需要了
                return
        node.is_leaf = True
        node.child = [None] * 26 #比word长的root不需要了
    
    def search(self, word):
        # print(word)
        node = self.root
        ret = ''
        flag = 0
        for i, w in enumerate(word):
            if w == ' ':
                return i + 1, ret
            if flag == 0:
                ret += w
            if flag == 1:
                ret += w
                continue
            if flag == 2:
                continue
            off = ord(w) - ord('a')
            if node.child[off] is None:
                flag = 1 #没有root，则一直循环到空格，然后return
            node = node.child[off]
            if node is not None and node.is_leaf:
                flag = 2 #找到了root，则一直循环到空格，但是中途的字母不要，然后return
        return -1, ret

if __name__ == '__main__':
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    # sentence = 'bbb baba'
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"

    dictionary = ["catt","cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"

    dictionary = ["ac","ab"]
    sentence = "it is abnormal that this solution is accepted"

    ret = Solution().replaceWords(dictionary, sentence)
    print(ret)