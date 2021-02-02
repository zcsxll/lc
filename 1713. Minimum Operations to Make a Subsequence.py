from typing import List

class Solution_tle:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        lcs = [[0] * (len(arr) + 1) for _ in range(len(target) + 1)]
        for i in range(1, len(target) + 1):
            for j in range(1, len(arr) + 1):
                lcs[i][j] = max(lcs[i-1][j-1] + int(target[i-1] == arr[j-1]),
                                lcs[i-1][j], lcs[i][j-1])
        # for line in lcs:
        #     print(line)
        return len(target) - lcs[-1][-1]

from bisect import bisect_left

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        m = {x:i for i, x in enumerate(target)}
        arr = [m[x] for x in arr if x in m]
        
        if len(arr) == 0:
            return len(target)

        dp = []
        for x in arr:
            if len(dp) == 0 or dp[-1] < x:
                dp.append(x)
            else:
                dp[bisect_left(dp, x)] = x
        # print(lis)
        return len(target) - len(dp)

target = [5,1,3]
arr = [9,4,2,3,4]
# target = [6, 4, 8, 1, 3, 2]
# arr = [4, 7, 6, 2, 3, 8, 6, 1]
# target = [1, 3, 8]
# arr = [2, 6]
print(Solution().minOperations(target, arr))