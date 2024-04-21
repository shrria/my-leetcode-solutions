class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        MAX_INT = 2**31 - 1

        if x > MAX_INT or x < -(MAX_INT + 1):
            return 0

        isNeg = x < 0
        if isNeg:
            x *= -1

        x_str = str(x)[::-1]
        if isNeg:
            x_str = "-" + x_str

        new_x = int(x_str)

        if new_x > MAX_INT or new_x < -(MAX_INT + 1):
            return 0

        return new_x


if __name__ == "__main__":
    s = Solution()

    testcase1 = 123
    testcase2 = -120
    testcase3 = 9646324351

    print(s.reverse(testcase1))
    print(s.reverse(testcase2))
    print(s.reverse(testcase3))
