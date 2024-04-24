class Solution(object):
    def minOperations(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        if k == 0:
            for i in range(len(nums1)):
                if nums1[i] != nums2[i]:
                    return -1
            return 0

        owe = 0
        counter = 0

        for i in range(len(nums1)):
            d = nums1[i] - nums2[i]
            if d == 0:
                continue

            if d % k:
                return -1

            mult = d // k
            counter += mult if mult > 0 else -mult
            owe += d

        if owe != 0:
            return -1

        return counter // 2


if __name__ == "__main__":
    s = Solution()

    testcase1 = [[4, 3, 1, 4], [1, 3, 7, 1], 3]
    testcase2 = [[3, 8, 5, 2], [2, 4, 1, 6], 1]
    testcase3 = [[0, 0, 1], [0, 0, 2], 0]

    print(s.minOperations(*testcase1))
    print(s.minOperations(*testcase2))
    print(s.minOperations(*testcase3))
