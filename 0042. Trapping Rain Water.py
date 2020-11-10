from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l, r = 0, len(height)-1
        max_l, max_r = 0, 0
        ret = 0
        while l < r: #从两边向中间
            if height[l] < height[r]: #优先处理低的
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    ret += (max_l - height[l]) #此时左边最高的比当前的高，且此时右边比左边高
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    ret += (max_r - height[r])
                r -= 1
        return ret

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(Solution().trap(height))
