# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        while root:
            if root.left:
                self._print_tree(root)

                flat_left = self._flatten_left(root.left)
                last_left_node = self._get_last_node(flat_left)
                last_left_node.right = root.right
                root.right = flat_left
                root = root.last_left_node
            root = root.right

    def _flatten_left(self, root):
        if root.left is None and root.right is None:
            return root

        flat_left = self._flatten_left(root.left)
        last_left_node = self._get_last_node(flat_left)
        last_left_node.right = root.right
        root.right = flat_left

    def _get_last_node(self, root):
        if root is None:
            return

        while root.right:
            if root.right is None:
                return root
            root = root.right

        return root

    def _print_tree(self, root):
        if root is None:
            return

        print(root.val)
        self._print_tree(root.left)
        self._print_tree(root.right)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))
    )
    s.flatten(root)
    print(root)
