import numpy as np
from typing import List

class Solution_old:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) <= 0:
            return False

        ret = np.zeros(len(s)).astype(bool)
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if j == 0 and s[:i+1] in wordDict:
                    ret[i] = True
                elif ret[j-1] == 1 and s[j:i+1] in wordDict:
                    ret[i] = True
        return ret[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) <= 0:
            return False

        ret = np.zeros(len(s)).astype(bool)
        ok_list = set()
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                ret[i] = True
                ok_list.add(i)
            else:
                for ok_idx in ok_list:
                    # print(i, ok_idx)
                    if s[ok_idx+1:i+1] in wordDict:
                        ret[i] = True
                        ok_list.add(i)
                        break
        # print(ret.astype(int))
        return ret[-1]

if __name__ == "__main__":
    s = "applepenapples"
    wordDict = ["apple", "pen", "s"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ret = Solution().wordBreak(s, wordDict)
    print(ret)