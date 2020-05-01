from typing import List
import numpy as np

class Solution:
    def candy(self, ratings: List[int]) -> int:
        zcs1 = np.ones_like(ratings)
        zcs2 = np.ones_like(ratings)
        for i in range(1, len(ratings)): #正序遍历ratings，如果是升序部分，则糖果数为左边的糖果数+1
            if ratings[i] > ratings[i-1]:
                zcs1[i] = zcs1[i-1] + 1

        ret = np.max((zcs1[-1], zcs2[-1]))
        for i in range(len(ratings) - 2, -1, -1): #倒序遍历ratings，如果是升序部分，则糖果数为右边的糖果数+1
            if ratings[i] > ratings[i+1]:
                zcs2[i] = zcs2[i+1] + 1
            ret += np.max((zcs1[i], zcs2[i])) #取两次遍历得到的糖果数的最大值

        # print(zcs1)
        # print(zcs2)
        return ret

if __name__ == "__main__":
    ratings = [1, 0, 2]
    ret = Solution().candy(ratings)
    print(ret)