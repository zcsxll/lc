from typing import List
import time
import copy

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # N = len(nums)
        # M = [[0x7fffffff]*N for i in range((m+1))]
        # M[1][0] = nums[0] #第0个数字分成一部分，则结果是nums[0]
        # for i in range(1, N):
        #     M[1][i] = M[1][i-1]+nums[i]
        # sumarr = copy.copy(M[1])
        # # for line in M:
        # #     print(line)
        # for i in range(2, m+1):
        #     for j in range(i-1, N):
        #         for k in range(i-1, j+1):
        #             tmp = max(M[i-1][k-1], sumarr[j]-sumarr[k-1])
        #             M[i][j] = min(M[i][j], tmp)
        #             # if M[i][j] > tmp:
        #             #     M[i][j] = tmp
        # # for line in M:
        # #     print(line)
        # return M[-1][-1]
        r = sum(nums)
        l = max(nums)
        while l < r:
            mid = (l + r) // 2
            if self.judge(nums, m, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def judge(self, nums, m, max_sum):
        '''
        遍历数组并求和，一旦和大雨max_sum，则分组加一
        且求和从当前数开始；一旦分组大于m，说明max_sum小了
        如果分组数小于m，则说明max_sum大了
        通过二分查找来确定max_sum，即为答案
        '''
        s = 0
        cnt = 0
        for n in nums:
            if s + n > max_sum:
                cnt += 1
                if cnt >= m:
                    return False
                s = n
            else:
                s += n
        return True

nums = [7,2,5,10,8, 4, 5, 6, 7, 8, 9, 3, 4, 5, 6, 6, 7, 5, 4, 3, 2, 4, 5, 6, 7, 8]
m = 10
nums = [1,2,3,4,5]
m = 2
# nums = [1, 4, 4]
# m = 3
nums = [7,2,5,10,8]
m = 2
st = time.time()
print(Solution().splitArray(nums, m))
et = time.time()
print(et-st)