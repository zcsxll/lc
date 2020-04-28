from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.mem = dict()
        """
        递归的时候可能遇到重复情况，比如输入是aaaa，字典是a aa aaa aaaa
        检测到a在字典中，则递归处理后缀aaa，然后再次检测到a在字典中，递归处理后缀aa
        第一次处理还会检测到aa在字典中，因此递归处理aa，这时候就出现多次处理后缀aa的情况了。
        """
        return self.zcs(s, wordDict)

    def zcs(self, s, wordDict):
        if s in self.mem:
            return self.mem[s]
        if s == "":
            return [""]
        # print(s)
        ret = []
        for word in wordDict:
            if s[:len(word)] == word:
                child_ret = self.zcs(s[len(word):], wordDict)
                if len(child_ret) > 0:
                    for a in child_ret:
                        ret.append((word + " " + a) if a != "" else word)
        self.mem[s] = ret
        return ret






























if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    ret = Solution().wordBreak(s, wordDict)
    print(ret)