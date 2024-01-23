class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        print()
        print("s", s)
        print("t", t)

        if len(s) != len(t):
            print("len(s) != len(t)")
            return False

        strMapS = dict()
        strMapT = dict()

        for i in range(len(s)):
            if s[i] not in strMapS:
                strMapS[s[i]] = []
            if t[i] not in strMapT:
                strMapT[t[i]] = []

            m = len(strMapS[s[i]])
            n = len(strMapT[t[i]])

            if m != n:
                print("m, n", (m, n))
                return False

            if m > 0 and strMapS[s[i]][-1] != strMapT[t[i]][-1]:
                print(strMapS[s[i]], strMapT[t[i]])
                return False

            strMapS[s[i]].append(i)
            strMapT[t[i]].append(i)

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("ab", "aa"))
    print(s.isIsomorphic("egg", "add"))
    print(s.isIsomorphic("foo", "bar"))
    print(s.isIsomorphic("paper", "title"))
    print(s.isIsomorphic("badc", "baba"))
    print(s.isIsomorphic("a", "a"))
