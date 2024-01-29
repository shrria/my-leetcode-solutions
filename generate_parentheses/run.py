class Solution:
    def generate(self, n):
        self.ans = []
        self.n = n

        self._generate("", 0, 0)

    def _generate(self, current, open_c, close_c):
        if len(current) == 2 * self.n:
            self.ans.append(current)
            return

        if open_c < self.n:
            self._generate(current + "(", open_c + 1, close_c)

        opening_c = open_c - close_c
        if opening_c > 0:
            self._generate(current + ")", open_c, close_c + 1)


if __name__ == "__main__":
    s = Solution()

    testCases = [1, 2, 3, 4, 5]

    for testCase in testCases:
        print("input:", testCase)
        s.generate(testCase)
        print("output:", s.ans, end="\n\n")
