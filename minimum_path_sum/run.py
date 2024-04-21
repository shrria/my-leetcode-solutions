class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.saved = [[None for _ in range(self.n)] for _ in range(self.m)]

        ## Initialization
        self.saved[0][0] = grid[0][0]

        for j in range(1, self.n):
            self.saved[0][j] = self.saved[0][j - 1] + grid[0][j]
        for i in range(1, self.m):
            self.saved[i][0] = self.saved[i - 1][0] + grid[i][0]

        ## Computing Cost Table
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.saved[i][j] = (
                    min(self.saved[i - 1][j], self.saved[i][j - 1]) + grid[i][j]
                )

        return self.saved[-1][-1]


if __name__ == "__main__":
    s = Solution()

    testcase1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    testcase2 = [[1, 2, 3], [4, 5, 6]]

    print(s.minPathSum(testcase1))
    print(s.minPathSum(testcase2))
