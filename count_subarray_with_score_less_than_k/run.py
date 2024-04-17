class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currentSum = 0
        left = 0
        right = 0
        counter = 0

        while right < len(nums):
            currentSum += nums[right]

            while currentSum * (right - left + 1) >= k and left <= right:
                currentSum -= nums[left]
                left += 1

            counter += right - left + 1

            right += 1

        return counter


if __name__ == "__main__":
    s = Solution()

    testcase1 = [[2, 1, 4, 3, 5], 10]
    testcase2 = [[1, 1, 1], 5]

    print(s.countSubarrays(*testcase1))
    print(s.countSubarrays(*testcase2))
