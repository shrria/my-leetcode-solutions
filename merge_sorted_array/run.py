class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        full_len = m + n

        while len(nums2) != 0:
            n2 = nums2.pop(0)
            for i in range(len(nums1)):
                n1 = nums1[i]
                if n1 == 0 and i >= m:
                    nums1[i] = n2
                    m += 1
                    break
                elif n2 <= n1:
                    tmp = nums1[i : full_len - 1]
                    nums1[i] = n2
                    nums1[i + 1 :] = tmp
                    m += 1
                    break


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    s.merge(nums1, m, nums2, n)

    print("nums1:", nums1)
