class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        result = self.countAndSay(n - 1)
        countString = self.countToString(result)
        return countString

    def countToString(self, text):
        result = ""

        cur = text[0]
        counter = 0
        for c in text:
            if cur == c:
                counter += 1
            else:
                result += str(counter) + cur
                cur = c
                counter = 1

        result += str(counter) + cur
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(5))
