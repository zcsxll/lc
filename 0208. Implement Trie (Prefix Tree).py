class Node:
    def __init__(self):
        self.childs = [None] * 26
        self.is_leaef = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            n = ord(w) - ord('a')
            if node.childs[n] is None:
                node.childs[n] = Node()
            node = node.childs[n]
        node.is_leaef = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            n = ord(w) - ord('a')
            if node.childs[n] is None:
                return False
            node = node.childs[n]
        return node.is_leaef

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            n = ord(w) - ord('a')
            if node.childs[n] is None:
                return False
            node = node.childs[n]
        return True
        
if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    obj.insert('app')
    print(obj.search('app'))
    print(obj.startsWith('app'))