class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) != len(word2):
            return False

        map1 = {}
        map2 = {}

        for i in range(len(word1)):
            c1 = word1[i]
            c2 = word2[i]

            if c1 not in map1:
                map1[c1] = 0
            if c2 not in map2:
                map2[c2] = 0

            map1[c1] = map1[c1] + 1
            map2[c2] = map2[c2] + 1

        if len(map1.keys()) != len(map2.keys()):
            return False

        key1 = []
        key2 = []
        val1 = []
        val2 = []

        for k, v in map1.items():
            key1.append(k)
            val1.append(v)

        for k, v in map2.items():
            key2.append(k)
            val2.append(v)

        key1.sort()
        key2.sort()
        val1.sort()
        val2.sort()

        # print("key1", key1)
        # print("key2", key2)
        # print("val1", val1)
        # print("val2", val2)

        return list(key1) == list(key2) and list(val1) == list(val2)


if __name__ == "__main__":
    s = Solution()

    testcase1 = ["abc", "bca"]
    testcase2 = ["a", "aa"]
    testcase3 = ["cabbba", "abbccc"]
    testcase4 = ["aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"]

    # print(s.closeStrings(*testcase1))
    # print(s.closeStrings(*testcase2))
    # print(s.closeStrings(*testcase3))
    print(s.closeStrings(*testcase4))
