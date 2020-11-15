from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        zcs = [0]*(300+1) #0 <= nums.length <= 300
        for n in nums:
            if 1 <= n <= 300:
                zcs[n] = 1
        for i, n in enumerate(zcs[1:]):
            if n == 0:
                return i+1

nums = [1, 2, 0]
nums = [7, 8, 9, 11, 12]
nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))