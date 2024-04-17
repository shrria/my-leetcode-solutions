class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        answers = [0] * len(nums)

        answers[:2] = nums[:2]
        answers[2] = nums[0] + nums[2]

        for i in range(3, len(nums)):
            answers[i] = max(answers[i - 2], answers[i - 3]) + nums[i]

        print("answers", answers)

        return max(answers[len(nums) - 1], answers[len(nums) - 2])


if __name__ == "__main__":
    s = Solution()

    testcase1 = [1, 2, 3, 1]
    testcase2 = [2, 7, 9, 3, 1]
    testcase3 = [1, 3, 1]

    print(s.rob(testcase1))
    print(s.rob(testcase2))
    print(s.rob(testcase3))
