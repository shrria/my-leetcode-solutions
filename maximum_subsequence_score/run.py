class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        pairValues = []

        for i in range(len(nums1)):
            pairValues.append((nums1[i], nums2[i]))

        pairValues.sort(key=lambda p: p[1], reverse=True)

        # print("pairValues", pairValues)
        # print()

        stack = []

        currentMinValue = 1e5
        currentMinMultIdx = 0
        currentTotal = 0
        for i in range(k):
            stack.append(pairValues[i])
            currentMinValue = min(stack[i][0], currentMinValue)
            if stack[i][1] < stack[currentMinMultIdx][1]:
                currentMinMultIdx = i
            currentTotal += stack[-1][0]

        currentMaxScore = stack[currentMinMultIdx][1] * currentTotal

        for i in range(k, len(nums1)):
            if pairValues[i][0] < currentMinValue:
                continue

            newStack = stack[:]
            newMinValue = currentMinValue
            newMinMultIdx = currentMinMultIdx
            newTotal = currentTotal
            newMaxScore = currentMaxScore

            for i_s in range(len(stack)):
                # print("run:", "i", i, "i_s", i_s)

                if (
                    pairValues[i][0] < stack[i_s][0]
                    and pairValues[i][1] < stack[i_s][1]
                ):
                    continue

                tmpStack = stack[:]
                tmpStack[i_s] = pairValues[i]

                # print("\ttmpStorage", tmpStack)

                tmpMinValue = 1e5
                tmpMinMultIdx = 0
                tmpTotal = 0
                for j in range(len(tmpStack)):
                    tmpMinValue = min(tmpStack[j][0], tmpMinValue)
                    if tmpStack[j][1] < tmpStack[tmpMinMultIdx][1]:
                        tmpMinMultIdx = j
                    tmpTotal += tmpStack[j][0]

                tmpScore = tmpStack[tmpMinMultIdx][1] * tmpTotal

                if tmpScore > newMaxScore:
                    # print("\t\tswap:", "i", i, "i_s", i_s)
                    # print(
                    #     "\ttmpScore:",
                    # )
                    # print("\t\ttmpMinMultIdx:", tmpMinMultIdx)
                    # print("\t\ttmpTotal:", tmpTotal)
                    newMinValue = tmpMinValue
                    newMinMultIdx = tmpMinMultIdx
                    newTotal = tmpTotal
                    newMaxScore = tmpScore
                    newStack = tmpStack[:]

            if newMaxScore > currentMaxScore:
                currentMinValue = newMinValue
                currentMinMultIdx = newMinMultIdx
                currentTotal = newTotal
                currentMaxScore = newMaxScore
                stack = newStack[:]

        return currentMaxScore


if __name__ == "__main__":
    s = Solution()

    testcase1 = [[1, 3, 3, 2], [2, 1, 3, 4], 3]
    testcase2 = [[4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1]
    testcase3 = [[2, 1, 14, 12], [11, 7, 13, 6], 3]

    print(s.maxScore(*testcase1))
    print(s.maxScore(*testcase2))
    print(s.maxScore(*testcase3))
