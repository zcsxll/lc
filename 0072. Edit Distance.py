class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1
        M = [[0 for _ in range(len2)] for _ in range(len1)]
        M[0][0] = 0 if word1[0] == word2[0] else 1

        for y in range(1, len1):
            M[y][0] = y if word1[y] == word2[0] else M[y-1][0] + 1

        for x in range(1, len2):
            M[0][x] = x if word2[x] == word1[0] else M[0][x-1] + 1

        for y in range(1, len1):
            for x in range(1, len2):
                if word1[y] == word2[x]:
                    M[y][x] = M[y-1][x-1]
                else:
                    M[y][x] = min(M[y-1][x-1], M[y-1][x], M[y][x-1]) + 1
        
        for line in M:
            print(line)
        return M[-1][-1]

word1 = "horse"
word2 = "ros"
# word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
# word2 = "ultramicroscopically"
print(Solution().minDistance(word1, word2))