from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0 #初始认为从0开始
        zcs = 0
        total = 0 #总的汽油量和消耗量的差，如果小于0则说明无法完成，会返回-1
        for idx, g in enumerate(gas):
            zcs = zcs + g - cost[idx]
            total = total + g - cost[idx]
            if zcs < 0: #如果小于0，说明无论无idx之前的哪个站出发，都不行
                zcs = 0
                start = idx + 1 #所以start改为idx + 1
        # print(total, start)
        return -1 if total < 0 else start


if __name__ == "__main__":
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    gas  = [2,3,4]
    cost = [3,4,3]

    has = [3,1,1]
    cost = [1,2,2]
    ret = Solution().canCompleteCircuit(gas, cost)
    print(ret)