from typing import List
import numpy as np

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        ret = np.zeros((n, n), dtype=np.int)

        for i in range(2, n):
            for a in range(0, n-i):
                for b in range(a+1, a + i):
                    ret[a][a+i] = max(ret[a][a+i], ret[a][b] + ret[b][a+i] + nums[a] * nums[b] * nums[a+i])
                # print(ret)
            # print()
        return ret[0][-1]

if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    ret = Solution().maxCoins(nums)
    print(ret)