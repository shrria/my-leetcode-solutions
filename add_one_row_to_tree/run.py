# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            root = TreeNode(val, left=root)
            return root

        self.addOneRow_(root, val, depth, 2)
        return root

    def addOneRow_(self, root, val, depth, curDepth):
        if curDepth > depth:
            return

        elif curDepth < depth:
            if root.left:
                self.addOneRow_(root.left, val, depth, curDepth + 1)

            if root.right:
                self.addOneRow_(root.right, val, depth, curDepth + 1)

        elif curDepth == depth:
            root.right = TreeNode(val, right=root.right)
            root.left = TreeNode(val, left=root.left)
