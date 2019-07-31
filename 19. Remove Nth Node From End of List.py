19. Remove Nth Node From End of List (Medium)

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# one pass
class Solution(object):
    count = 0
    removed = False
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.removeNthFromEnd_v2(head, n)
        if not self.removed:
            head=head.next

        return head

    def removeNthFromEnd_v2(self, head, n):
        if head.next:
            self.removeNthFromEnd_v2(head.next, n)
        self.count = self.count + 1
        if self.count == n+1:
            head.next = head.next.next
            self.removed = True
        return head


# 2 pass, faster
class Solution(object):
    count = 0
    removed = False
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        head_temp=head
        while head_temp is not None:
            count = count + 1
            head_temp=head_temp.next
        if count == n:
            return head.next
        i=1
        head_temp=head
        while i < count-n:
            i=i+1
            head_temp=head_temp.next
        head_temp.next = head_temp.next.next
        return head

