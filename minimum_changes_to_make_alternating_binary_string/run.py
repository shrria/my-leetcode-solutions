class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        diff0 = 0
        diff1 = 0

        for i in range(len(s)):
            if (i + 1) % 2:
                if s[i] != "0":
                    diff0 += 1
                else:
                    diff1 += 1
            else:
                if s[i] != "0":
                    diff1 += 1
                else:
                    diff0 += 1

        return min(diff0, diff1)


if __name__ == "__main__":
    s = Solution()

    testcase1 = "0100"
    testcase2 = "10"
    testcase3 = "1111"

    print(s.minOperations(testcase1))
    print(s.minOperations(testcase2))
    print(s.minOperations(testcase3))
