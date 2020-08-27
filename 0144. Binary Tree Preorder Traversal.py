from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret = []
        self.zcs(root)
        return self.ret

    def zcs(self, node):
        if node is None:
            return
        self.ret.append(node.val)
        self.zcs(node.left)
        self.zcs(node.right)

def make_tree(seq, idx):
    if idx >= len(seq) or seq[idx] == '#':
        return None
    node = TreeNode(seq[idx])
    node.left = make_tree(seq, idx * 2 + 1)
    node.right = make_tree(seq, idx * 2 + 2)
    return node