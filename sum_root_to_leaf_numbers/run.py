# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.result = 0

        self.depthFirstSum(0, root)

        return self.result

    def depthFirstSum(self, number, cur_node):
        number = number * 10 + cur_node.val

        if cur_node.left is None and cur_node.right is None:
            self.result += number
            return

        if cur_node.left:
            self.depthFirstSum(number, cur_node.left)

        if cur_node.right:
            self.depthFirstSum(number, cur_node.right)


if __name__ == "__main__":
    s = Solution()

    testNodes = [
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)),
    ]

    for testCase in testNodes:
        # print("input:", testCase)
        s.sumNumbers(testCase)
        print("output:", s.result, end="\n\n")
