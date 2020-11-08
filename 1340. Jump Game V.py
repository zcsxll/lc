from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        z = sorted(enumerate(arr), key=lambda x : x[1])
        '''
        只能向更低的位置跳，因此需要从低到高进行遍历
        但是不能破坏原有顺序，所以这里排序后保留原有的index
        从低到高遍历时，从更低的位置起跳能跳跃的最大次数已经计算得到了
        是DP解法
        '''
        # print(z)
        N = len(arr)
        ret = [1]*N
        for pos, height in z: #从低到高遍历
            end = min(pos+d+1, N) #向右跳，根据d获取跳跃范围
            for i in range(pos+1, end): #再能跳跃的范围依次判断
                if height <= arr[i]: #遇到更高的，就只能停止，不能继续向右跳了
                    break
                ret[pos] = max(ret[pos], ret[i]+1) #如果跳跃到这个位置，则最大次数时这个位置的最大值+1
            end = max(-1, pos-d-1) #向左跳
            for i in range(pos-1, end, -1):
                if height <= arr[i]:
                    break
                ret[pos] = max(ret[pos], ret[i]+1)
        # print(ret)
        return max(ret)

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
arr = [3, 3, 3, 3]
d = 3
arr = [7, 6, 5, 4, 3, 2, 1]
d = 1
print(Solution().maxJumps(arr, d))