class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = '#' + s
        V = [0] * len(s)
        ret = 0
        for i in range(2, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    V[i] = V[i-2] + 2
                else:
                    idx = i - 1 - V[i-1]
                    if s[idx] == '(':
                        V[i] = V[i-1] + 2 + V[idx-1]
                if ret < V[i]:
                    ret = V[i]
        # print(V)
        # print(ret)
        return ret

s = "(()"
s = ")()())"
s = "(())())"
ret = Solution().longestValidParentheses(s)
print(ret)