class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        ret = ''
        while num != 0:
            n = num & 0xf
            # print('%x' % num)
            num >>= 4
            num &= 0x0fffffff
            # print('%x' % num)
            if n < 10:
                ret = chr(ord('0')+n)+ret
            else:
                ret =  chr(ord('a')+n-10)+ret
        return ret

n = 26
n = -1
print(Solution().toHex(n))