from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = [0] * len(nums)
        flag[0] = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if flag[j] == 1 and nums[j] + j >= i:
                    flag[i] = 1
                    break
            if flag[i] == 0:
                return False
        return True

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(Solution().canJump(nums))