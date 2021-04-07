from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            len1, len2 = len2, len1
        if len1 * 6 < len2:
            return -1

        sum1, sum2 = 0, 0
        d1 = [0 for _ in range(7)]
        d2 = [0 for _ in range(7)]
        for n in nums1:
            sum1 += n
            d1[n] += 1

        for n in nums2:
            sum2 += n
            d2[n] += 1

        if sum1 < sum2:
            sum1, sum2 = sum2, sum1
            d1, d2 = d2, d1

        idx1 = 6
        while d1[idx1] == 0:
            idx1 -= 1

        idx2 = 1
        while d2[idx2] == 0:
            idx2 += 1

        count = 0
        while sum1 > sum2:
            count += 1
            if idx1 - 1 > 6 - idx2:
                sum1 -= (idx1 - 1)
                d1[idx1] -= 1
                while idx1 >= 1 and d1[idx1] <= 0:
                    idx1 -= 1
            else:
                sum2 += (6 - idx2)
                d2[idx2] -= 1
                while idx2 <= 6 and d2[idx2] <= 0:
                    idx2 += 1
        # print(count)
        return count

if __name__ == '__main__':
    nums1 = [1,2,3,4,5,6]
    nums2 = [1,1,2,2,2,2]
    # nums1 = [1, 1, 1, 1, 1, 1, 1]
    # nums2 = [6]

    # nums1 = [6, 6]
    # nums2 = [1]

    ret = Solution().minOperations(nums1, nums2)
    print(ret)