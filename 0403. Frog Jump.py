from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        M = [set() for s in stones] #M[i]存储从第i个石头可以起跳的距离
        M[0].add(1) #依据题意，第0个石头的起跳距离只有1
        # print(M)

        for i in range(1, len(stones)):
            for j in range(i): #检测第i个石头之前的全部石头
                dis = stones[i] - stones[j]
                if dis in M[j]: #如果可以从i之前的石头j跳过来
                    M[i].add(dis-1) #则石头i的起跳距离多了三个
                    M[i].add(dis)
                    M[i].add(dis+1)
        # print(M)
        return len(M[-1]) > 0

stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]
print(Solution().canCross(stones))