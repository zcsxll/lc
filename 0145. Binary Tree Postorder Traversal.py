from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        zcs = [] #list，append会在最后加入一个元素，pop会弹出最后的元素，和栈一样的逻辑
        ret = []
        if root is not None:
            zcs.append(root)
        while len(zcs) > 0:
            node = zcs.pop()
            ret.insert(0, node.val)
            if node.left is not None:
                zcs.append(node.left)
            if node.right is not None:
                zcs.append(node.right)
        # print(ret)
        return ret

def make_tree(seq, idx):
    if idx >= len(seq) or seq[idx] == '#':
        return None
    node = TreeNode(seq[idx])
    node.left = make_tree(seq, idx * 2 + 1)
    node.right = make_tree(seq, idx * 2 + 2)
    return node

if __name__ == "__main__":
    root = make_tree([1, 2, 3, 4, 5, 6], 0)
    ret = Solution().postorderTraversal(root)
    print(ret)