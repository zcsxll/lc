class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        ret = 0
        flag = 0
        for val in m.values():
            if flag == 0 and val % 2 == 1:
                flag = 1
            ret += ((val // 2) * 2)
        ret += flag
        return ret

s = "abccccdd"
print(Solution().longestPalindrome(s))