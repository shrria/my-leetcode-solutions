
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        print("     ", end=" ")
        for c in word2:
            print(c, end=", ")

        print()
        for i in range(len(dp)):
            print(word1[i - 1] if i > 0 else " ", end=" ")
            print(dp[i])

        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print("ans", s.minDistance("horse", "xorsx"))