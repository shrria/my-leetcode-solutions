# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Handle one node
        if head.next is None:
            return True

        # Handle two nodes
        if head.next.next is None:
            return head.val == head.next.val

        stack = []
        fastPointer = head
        slowPointer = head
        while fastPointer.next and fastPointer.next.next:
            stack.append(slowPointer.val)
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        isEven = fastPointer.next is not None
        if isEven:
            stack.append(slowPointer.val)

        slowPointer = slowPointer.next

        while len(stack):
            if stack.pop(-1) != slowPointer.val:
                return False
            slowPointer = slowPointer.next

        return True


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
