class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1

        # print("n:", n)

        start_point = n // 2 + 1
        for i in range(start_point, n - 1):
            sum_start = i * (i + 1) // 2

            sum_end = 0
            for j in range(i + 2, n + 1):
                sum_end += j

            # print("i:", i, "sum:", sum_start, ",", sum_end)
            if sum_start == sum_end:
                return i + 1

        return -1


if __name__ == "__main__":
    s = Solution()

    for i in range(1, 21):
        print()
        print(s.pivotInteger(i))
