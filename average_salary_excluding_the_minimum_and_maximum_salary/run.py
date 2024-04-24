class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        max_idx = 0
        min_idx = 0

        total = salary[0]

        for i in range(1, len(salary)):
            if salary[i] > salary[max_idx]:
                max_idx = i

            elif salary[i] < salary[min_idx]:
                min_idx = i

            total = total + salary[i]

        avg = (total - salary[max_idx] - salary[min_idx]) / (len(salary) - 2)

        return avg


if __name__ == "__main__":
    s = Solution()

    testcase1 = [4000, 3000, 1000, 2000]
    testcase2 = [1000, 2000, 3000]
    testcase3 = [6000, 5000, 4000, 3000, 2000, 1000]
    testcase4 = [8000, 9000, 2000, 3000, 6000, 1000, 7000, 4000, 5000]
    testcase5 = [
        48000,
        59000,
        99000,
        13000,
        78000,
        45000,
        31000,
        17000,
        39000,
        37000,
        93000,
        77000,
        33000,
        28000,
        4000,
        54000,
        67000,
        6000,
        1000,
        11000,
    ]

    print(s.average(testcase1))
    print(s.average(testcase2))
    print(s.average(testcase3))
    print(s.average(testcase4))
    print(s.average(testcase5))
