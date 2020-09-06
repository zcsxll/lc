from typing import List
import numpy as np

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        M = np.zeros((n, n), dtype=np.int)

        for k in range(2, n): #k=2时是计算戳破1个气球的最优解，k=3时事计算戳破2个连续的气球的最优解。。。
            for a in range(0, n-k): #a是被戳破的连续K-1个气球的区间的左边，a+k是区间的右边
                for i in range(a+1, a+k): #i就是上述分析中的i
                    M[a][a+k] = max(M[a][a+k], M[a][i] + M[i][a+k] + nums[a] * nums[i] * nums[a+k])
        return M[0][-1]

if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    ret = Solution().maxCoins(nums)
    print(ret)