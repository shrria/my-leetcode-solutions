class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mapping = mapping

        pairValues = []

        for num in nums:
            val = self.convertJumbled(num)
            pairValues.append((val, num))

        pairValues.sort(key=lambda p: p[0])

        result = []

        for pair in pairValues:
            result.append(pair[1])

        return result

    def convertJumbled(self, input):
        strNum = str(input)
        value = 0
        for c in strNum:
            value = value * 10 + self.mapping[int(c)]
        return value


if __name__ == "__main__":
    s = Solution()

    testMapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    testNums = [991, 338, 38]

    s.sortJumbled(testMapping, testNums)
