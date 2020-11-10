from typing import List
import functools

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        key = functools.cmp_to_key(lambda x, y : y[0]-x[0] if x[0] != y[0] else x[1]-y[1])
        people.sort(key=key) #按身高降序，后面的数字升序排序
        # print(people)
        ret = []
        for p in people: #这样一个个插入到新队列就是答案
            ret.insert(p[1], p)
        return ret

q = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(q))