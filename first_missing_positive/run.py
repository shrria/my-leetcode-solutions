class Solution(object):
    def firstMissingPositive(self, nums):
        i = 0
        n = len(nums)

        while i < n:
            crt = nums[i] - 1
            if nums[i] > 0 and nums[i] < n and nums[i] != nums[crt]:
                temp = nums[i]
                nums[i] = nums[crt]
                nums[crt] = temp
            else:
                i += 1

        print("nums:", nums)

        if nums[0] != 1:
            return 1

        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1

        return n + 1


if __name__ == "__main__":
    s = Solution()

    testCases = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [8, 7, 9, 11, 12],
    ]

    for testCase in testCases:
        print("input:", testCase)
        print("output:", s.firstMissingPositive(testCase), end="\n\n")
