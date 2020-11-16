from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        b1, b2, b3 = -2147483648.1, -2147483648.1, -2147483648.1
        cnt = 0
        for n in nums:
            if b1 < n:
                b1, b2, b3 = n, b1, b2
            elif b2 < n and n != b1:
                b2, b3 = n, b2
            elif b3 < n and n != b1 and n != b2:
                b3 = n
        return int(b3) if b3 > -2147483648.1 else int(b1)

nums = [3, 2, 0, 100]
# nums = [2, 2, 3, 1]
# nums = [1, 2]
# nums = [1, 2, -2147483648]

nums = [1,-2147483648,2]
nums = [1, 2]
print(Solution().thirdMax(nums))