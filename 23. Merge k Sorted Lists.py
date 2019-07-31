# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Very slow, but accepted, Approach 2: Compare one by one
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i=0
        while i < len(lists):
            if lists[i] is None or lists[i] == []:
                lists.remove(lists[i])
            else:
                i=i+1
        if len(lists)<=0:
            return None
        self.find_min(lists)
        head = lists[0]
        current = head
        lists[0] = lists[0].next
        if lists[0] is None:
            lists.remove(lists[0])
        if len(lists)<=0:
            return head
        while len(lists)>1:
            self.find_min(lists)
            current.next=lists[0]
            current = current.next
            lists[0] = lists[0].next
            if lists[0] is None:
                lists.remove(lists[0])
        current.next=lists[0]
        return head
    #
    def find_min(self,lists):
        temp_min = lists[0].val
        for i in range(1,len(lists)):
            if lists[i].val < temp_min:
                temp_min = lists[i].val
                temp = lists[i]
                lists[i] = lists[0]
                lists[0] = temp
        return 0


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a0 = ListNode(1)
a1 = ListNode(3)
a2 = ListNode(6)
a0.next=a1
a1.next=a2

b0 = ListNode(2)
b1 = ListNode(4)
b2 = ListNode(5)
b0.next=b1
b1.next=b2

c0 = ListNode(0)
c1 = ListNode(3.5)
c2 = ListNode(10)
c0.next=c1
c1.next=c2

l=[b0,a0,c0]

sol = Solution()
anw = sol.mergeKLists(l)
print_node(anw)

def print_node(node_a):
    while node_a is not None:
        print (node_a.val)
        node_a = node_a.next


