class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ret = ''
        carry = 0
        min_len = min(len(num1), len(num2))
        for i in range(-1, -min_len-1, -1):
            a = ord(num1[i])-ord('0')
            b = ord(num2[i])-ord('0')
            s = a+b+carry
            r = s % 10
            carry = s // 10
            ret = chr(r+ord('0'))+ret
        for i in range(-min_len-1, -len(num1)-1, -1):
            a = ord(num1[i])-ord('0')
            s = a+carry
            r = s % 10
            carry = s // 10
            ret = chr(r+ord('0'))+ret
        for i in range(-min_len-1, -len(num2)-1, -1):
            a = ord(num2[i])-ord('0')
            s = a+carry
            r = s % 10
            carry = s // 10
            ret = chr(r+ord('0'))+ret
        if carry == 1:
            ret = '1'+ret
        return ret

num1 = '423'
num2 = '999637'
print(Solution().addStrings(num1, num2))