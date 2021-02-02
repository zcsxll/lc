from typing import List

class Solution_ON2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        max_lis = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
                    max_lis = max(max_lis, lis[i])
        # print(max_lis)
        return max_lis

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            if len(lis) == 0 or n > lis[-1]:
                lis.append(n)
            else:
                lis[bisect_left(lis, n)] = n
        # print(max_lis)
        return len(lis)

if __name__ == '__main__':
    nums = [0,1,0,3,2,3]
    # nums = [7, 7, 7]
    ret = Solution().lengthOfLIS(nums)
    print(ret)