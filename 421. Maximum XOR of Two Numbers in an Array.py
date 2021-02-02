from typing import List

class Tree:
    def __init__(self):
        self.child = [None, None]

    def insert(self, num):
        node = self
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.child[bit] is None:
                node.child[bit] = Tree()
            node = node.child[bit]

    def query(self, num):
        node = self
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.child[1-bit] is None:
                node = node.child[bit]
            else:
                node = node.child[1-bit]
                xor += 1 << i
        return xor

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tree = Tree()
        for num in nums:
            tree.insert(num)
        max_xor = 0
        for num in nums:
            xor = tree.query(num)
            max_xor = max(max_xor, xor)
        return max_xor

nums = [3,10,5,25,2,8]
ret = Solution().findMaximumXOR(nums)
print(ret)