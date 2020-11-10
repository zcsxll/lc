from typing import List

import bisect

class Solution:
    # def insert(self, q, h, y, x):
    #         for i in range(len(q)):
    #             if q[i][0] >= h:
    #                 q.insert(i, (h, y, x))
    #                 return
    #         q.append((h, y, x)) 

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        Y, X = len(heightMap), len(heightMap[0])
        # flag = [[0]*X]*Y
        flag = [[0]*X for y in range(Y)]
        q = []
        for y in range(Y): #将最外边加入list中
            for x in range(X):
                if y == 0 or y == Y-1 or x == 0 or x == X-1:
                    q.append((heightMap[y][x], y, x))
                    flag[y][x] = 1
        # print(flag)
        q.sort(key=lambda x : x[0])
        # print(q)

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_h = 0
        ret = 0
        while q: #每次都取出最矮的
            h, y, x = q.pop(0)
            max_h = max(max_h, h)
            for dy, dx in direction: #向四周探索
                y2 = y + dy
                x2 = x + dx
                if x2 >= 0 and x2 < X and y2 >= 0 and y2 < Y and flag[y2][x2] == 0:
                    flag[y2][x2] = 1
                    if heightMap[y2][x2] < max_h: #此时必能存留雨水，如果x2 y2处的四周有比它矮的，那必定已经先前就被遍历了，不会执行到此处
                        ret += (max_h - heightMap[y2][x2])
                    # print(q, h, y, x)
                    # self.insert(q, heightMap[y2][x2], y2, x2) #效果一样，但是更慢
                    bisect.insort(q, (heightMap[y2][x2], y2, x2))
                    # print(q)
        return ret

heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(Solution().trapRainWater(heightMap))