class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        M = [[True] * n] * n
        
        if n <= 1:
            return s
        ret = s[0]
        max_len = 0
        for r in range(1, n):
            for l in range(0, r):
                M[r][l] = M[r-1][l+1] if s[l] == s[r] else False
                if M[r][l] and max_len < r - l + 1:
                    max_len = r - l + 1
                    ret = s[l:r+1]
        return ret


s = 'babad'
# s = 'cbbd'
# s = 'dfgh'
# s = 'abcda'
ret = Solution().longestPalindrome(s)
print(ret)