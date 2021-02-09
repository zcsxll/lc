class Node:
    def __init__(self):
        self.child = [None] * 26
        self.is_leaf = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            n = ord(w) - ord('a')
            if node.child[n] is None:
                node.child[n] = Node()
            node = node.child[n]
        node.is_leaf = True
            
    def search(self, word: str, node=None) -> bool:
        node = self.root if node is None else node
        for i, w in enumerate(word):
            if w == '.':
                for c in node.child:
                    if c is not None and self.search(word[i+1:], c):
                        return True
                return False
            n = ord(w) - ord('a')
            if node.child[n] is None:
                return False
            node = node.child[n]
        return node.is_leaf

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dad')
    obj.addWord('mad')

    print(obj.search('pad'))
    print(obj.search('bad'))
    print(obj.search('.ad'))
    print(obj.search('b..'))
    print(obj.search('b'))