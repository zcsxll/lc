from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        还可以用递归，比如判断第0个字符，肯定是回文，则加入列表，并将当前结果递归处理，只是处理的字符串变成[1:]，后续就不讲述了
        然后遍历到第1个字符，如果可以和第0个字符组成回文，则递归处理当前结果，只是处理的字符串变成[2:]
        然后遍历到第2个字符，如果可以和前两个字符组成回文，则递归处理当前结果，只是处理的字符串变成[3:]
        """
        ret = [[s[0]]] #初始化
        for c in s[1:]:
            cur_len = len(ret)
            for i in range(cur_len): #首先遍历已有列表，判断当前字符c能否和列表最后一个字符串，以及列表最后两个字符串组成回文，不存在其他情况了
                zcs = ret[i]
                ss = zcs[-1] + c
                if ss == ss[::-1]: #判断当前字符c能否和列表最后一个字符串组成回文
                    new_list = zcs[:-1] + [ss] #如果可以，则需要复制这个列表，并把最后一个字符串替换为新的组合
                    if new_list not in ret:
                        ret.append(new_list)
                if len(zcs) >= 2:
                    ss = zcs[-2] + zcs[-1] + c
                    if ss == ss[::-1]: #判断当前字符c能否和列表最后两个字符串组成回文
                        new_list = zcs[:-2] + [ss] #如果可以，则需要复制这个列表，并把最后两个字符串替换为新的组合
                        if new_list not in ret:
                            ret.append(new_list)
                ret[i] += c
            # print(ret)
        return ret


if __name__ == "__main__":
    ret = Solution().partition("cbbbcc")

    for line in ret:
        for p in line:
            print(p, end = " ")
        print()
    # print(board)