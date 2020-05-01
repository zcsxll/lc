import numpy as np

class Solution:
    def minCut(self, s: str) -> int:
        ok = np.zeros((len(s), len(s))) #ok[j][i]为1表示子串s[j:i+1]是回文。只使用上三角
        ret = np.ones(len(s)) * len(s) #动态规划后，会有len(s)个最优答案。初始化时用s的长度len(s)作为最糟糕的值即可，因为最多需要分割len(s)次

        for i in range(len(s)):
            for j in range(i, -1, -1): #从i循环到0
                if s[i] == s[j] and (i - j <= 1 or ok[j+1][i-1] == 1):
                    ok[j][i] = 1
                    if j == 0:
                        ret[i] = 0
                    elif ret[i] > ret[j - 1] + 1:
                        ret[i] = ret[j - 1] + 1

        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         print(ok[i][j], end = " ")
        #     print()

        return int(ret[-1])

if __name__ == "__main__":
    ret = Solution().minCut("aab")
    print(ret)