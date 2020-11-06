from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        M = [0] * (target+1)
        for t in range(1, target+1):
            for idx, c in enumerate(cost):
                idx += 1
                if t == c:
                    M[t] = max(M[t], idx)
                elif t > c and M[t-c] != 0:
                    print(M[t-c], idx, end=' ')
                    M[t] = max(M[t], 10*M[t-c]+idx)
                    print(M[t])
            print(M)
        return str(M[-1])

if __name__ == "__main__":
    cost = [4,3,2,5,6,7,2,5,5]
    target = 9

    cost = [7,6,5,5,5,6,8,7,8]
    target = 12

    # cost = [2,4,6,2,4,6,4,4,4]
    # target = 5
    # cost = [1,1,1,1,1,1,1,1,1]
    # target = 5000
    cost = [2, 3]
    target = 8
    ret = Solution().largestNumber(cost, target)
    print(ret)