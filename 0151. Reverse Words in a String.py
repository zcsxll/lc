class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1] + ' '
        print(s)
        s1 = 0
        e1 = 0
        ret = ''
        while e1 < len(s):
            if s[e1] == ' ':
                if s1 != e1:
                    # print("[%s]" % s[s1:e1])
                    # s[s2:s2+(e1-s1)] = s[e1-1:s1-1:-1]
                    # print(s)
                    ret += (s[s1:e1][::-1] + ' ')
                e1 += 1
                s1 = e1
            else:
                e1 += 1
        return ret[:-1]

if __name__ == "__main__":
    s = '  hello world!  '
    s = "the sky is blue"
    s = Solution().reverseWords(s)
    print('[%s]' % s)