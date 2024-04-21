class Solution(object):
    def getMinInRange(self, heights, l, r):
        min_val = heights[l]

        for i in range(l, r):
            min_val = min(min_val, heights[i])

        return min_val

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ## Approach 1
        ## Time Complexity: O(n)
        ## Space Complexity: O(n)

        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        stack = []
        max_area = 0
        stack.append(0)

        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area


if __name__ == "__main__":
    s = Solution()

    testcase1 = [2, 1, 2, 2, 2, 1]
    testcase2 = [2, 4]
    testcase3 = [4, 2]
    testcase4 = [0, 9]
    testcase5 = [3, 6, 5, 7, 4, 8, 1, 0]
    testcase6 = [4, 2, 0, 3, 2, 4, 3, 4]
    testcase7 = [3, 1, 3, 4, 2, 3]

    print(s.largestRectangleArea(testcase1))
    # print(s.largestRectangleArea(testcase2))
    # print(s.largestRectangleArea(testcase3))
    # print(s.largestRectangleArea(testcase4))
    # print(s.largestRectangleArea(testcase5))
    # print(s.largestRectangleArea(testcase6))
    print(s.largestRectangleArea(testcase7))
