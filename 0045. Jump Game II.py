from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # M = [len(nums)] * len(nums)
        # M[0] = 0
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[j] + j >= i and M[j] + 1 < M[i]:
        #             M[i] = M[j] + 1
        # return M[-1]

        farthest = 0
        last = 0
        steps = 0
        for i in range(len(nums)-1): #题目说坑定能到达最后节点，因此最后一个节点无需处理
            farthest = max(farthest, nums[i]+i) #从i处能跳的最远的位置
            if i == last:
                last = farthest #记录新的范围，后面会在i到last这个范围寻找能跳的最远的位置
                steps += 1
                if farthest >= len(nums) - 1:
                    break
        return steps

nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
nums = [0]
print(Solution().jump(nums))