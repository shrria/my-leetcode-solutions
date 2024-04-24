class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        counter = 0

        for n in arr:
            if self.isOdd(n):
                counter += 1
            else:
                counter = 0

            if counter == 3:
                return True

        return False

    def isOdd(self, num):
        return num % 2 == 1
