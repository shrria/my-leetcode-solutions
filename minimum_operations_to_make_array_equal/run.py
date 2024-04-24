class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n % 2:
            return (n - 1) ** 2 / 4 + (n - 1) / 2

        return n**2 / 4


if __name__ == "__main__":
    s = Solution()

    testcase1 = 1
    testcase2 = 2
    testcase3 = 3
    testcase4 = 4
    testcase5 = 5

    print(s.minOperations(testcase1))
    print(s.minOperations(testcase2))
    print(s.minOperations(testcase3))
    print(s.minOperations(testcase4))
    print(s.minOperations(testcase5))
