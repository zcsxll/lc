from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        flag = [0] * len(arr)
        return self.zcs(arr, start, flag)

    def zcs(self, arr, start, flag):
        print(start)
        if arr[start] == 0:
            return True

        pos = start + arr[start]
        if pos <= len(arr) - 1 and flag[pos] == 0:
            flag[pos] = 1    
            if self.zcs(arr, pos, flag):
                return True
        pos = start - arr[start]
        if pos >= 0 and flag[pos] == 0:
            flag[pos] = 1
            if self.zcs(arr, pos, flag):
                return True
        return False

arr = [4,2,3,0,3,1,2]
arr = [3, 0, 2, 1, 2]
start = 0
start = 2
print(Solution().canReach(arr, start))