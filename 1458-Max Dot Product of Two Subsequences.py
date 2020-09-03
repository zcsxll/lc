from typing import List
import numpy as np

class Solution:
    '''
    这个也是对的
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        M = np.zeros((len(nums1), len(nums2)), dtype=np.int)

        M[0][0] = nums1[0]*nums2[0]
        for i in range(1, len(nums1)):
            M[i][0] = max(M[i-1][0], nums1[i]*nums2[0])
        for j in range(1, len(nums2)):
            M[0][j] = max(M[0][j-1], nums1[0]*nums2[j])

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                M[i][j] = max(M[i-1][j-1]+nums1[i]*nums2[j], M[i][j-1], M[i-1][j], nums1[i]*nums2[j])
            print(M)
        return M[-1][-1]
        '''

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        M = [[-100000] * (n2 + 1)  for _ in range(n1 + 1)]

        for i in range(n1):
            for j in range(n2):
                M[i+1][j+1] = max(M[i][j]+nums1[i]*nums2[j], M[i][j+1], M[i+1][j], nums1[i]*nums2[j])
            # for i in range(n1 + 1):
            #     print(M[i])
            # print()
        return M[-1][-1]

if __name__ == '__main__':
    nums1 = [2,1,-2,5]
    nums2 = [3,0,-6]

    # nums1 = [-1, -1]
    # nums2 = [1, 1]

    # nums1 = [-3,-8, 3,-10, 1, 3, 9]
    # nums2 = [ 9, 2, 3,  7,-9, 1,-8, 5, -1, -1]

    ret = Solution().maxDotProduct(nums1, nums2)
    print(ret)