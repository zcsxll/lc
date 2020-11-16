from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s //= 2
        ret = [False]*(s+1)
        ret[0] = True
        for n in nums:
            for k in range(s, 0, -1):
                if k >= n and k-n <= s:
                    ret[k] = ret[k] or ret[k-n]
        # print(ret)
        return ret[-1]

nums = [1,5,11,5]
nums = [1, 2, 3, 5]
print(Solution().canPartition(nums))