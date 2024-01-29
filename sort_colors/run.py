class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count0 = 0
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            elif nums[i] == 2:
                count2 += 1

        nums[:count0] = [0] * count0
        nums[count0 : count0 + count1] = [1] * count1
        nums[count0 + count1 :] = [2] * count2

        return nums


if __name__ == "__main__":
    s = Solution()

    testCases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
    ]

    for testCase in testCases:
        print("input:", testCase)
        s.sortColors(testCase)
        print("output:", testCase, end="\n\n")
