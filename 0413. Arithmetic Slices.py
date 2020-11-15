from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        start = 0
        diff = A[1]-A[0]
        ret = 0
        for i in range(1, len(A)):
            if A[i]-A[i-1] == diff:
                continue
            if i-start >= 3:
                length = i-start
                end = length-3+1
                '''
                end是长度为3的ArithmeticSlice的数量
                长度为4的ArithmeticSlice的数量是end-1
                直到长度为length的ArithmeticSlice的数量为1
                总数是1+2+3+...+end
                '''
                ret += ((1+end)/2*end)
            start = i-1
            diff = A[i]-A[i-1]
        length = len(A)-start
        if length >= 3:
            # print('last', length)
            end = length-3+1
            ret += ((1+end)/2*end)
        return int(ret)

A = [1, 2, 3, 4, 6, 8, 10, 12]
print(Solution().numberOfArithmeticSlices(A))