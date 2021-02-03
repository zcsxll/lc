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
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.child[1-bit] is not None:
                max_xor += 1 << i
                node = node.child[1-bit]
            elif node.child[bit] is not None:
                node = node.child[bit]
            else:
                return -1
        return max_xor

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # list.sort(nums)
        nums.sort()
        for idx, query in enumerate(queries):
            query.append(idx)
        # print(queries)
        queries.sort(key=lambda x: x[1])
        tree = Tree()

        max_xors = [-1] * len(queries)
        off = 0
        for key, max_num, idx in queries:
            while off < len(nums) and nums[off] <= max_num:
                tree.insert(nums[off])
                off += 1
            max_xors[idx] = tree.query(key)
        return max_xors

nums = [0,1,2,3,4]
queries = [[3,1],[1,3],[5,6]]

# nums = [5,2,4,6,6,3]
# queries = [[12,4],[8,1],[6,3]]
ret = Solution().maximizeXor(nums, queries)
print(ret)