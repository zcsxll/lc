# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = []
        q.append((root, 0))
        ret = 0
        while q:
            node, flag = q.pop(0)
            if node.left is not None:
                q.append((node.left, 1))
            if node.right is not None:
                q.append((node.right, 0))
            if flag == 1 and node.left is None and node.right is None:
                ret += node.val
        return ret
        
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().sumOfLeftLeaves(root))