class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        currentProd = 1
        left = 0
        right = 0
        counter = 0

        while right < len(nums):
            currentProd *= nums[right]

            while currentProd >= k and left <= right:
                currentProd /= nums[left]
                left += 1

            counter += right - left + 1

            right += 1

        return counter


if __name__ == "__main__":
    s = Solution()

    testcase1 = [[10, 5, 2, 6], 100]
    testcase2 = [[1] * 2000, 85850]

    print(s.numSubarrayProductLessThanK(*testcase1))
    # print(s.numSubarrayProductLessThanK(*testcase2))
