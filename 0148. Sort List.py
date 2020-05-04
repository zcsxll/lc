class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        fast = head
        slow = head
        slow_pre = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow_pre = slow
            slow = slow.next
        slow_pre.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        ret = ListNode(-1)
        tail = ret
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1 is not None:
            tail.next = l1
        elif l2 is not None:
            tail.next = l2
        # print_list(ret)
        return ret.next

def print_list(head):
    while head is not None:
        print("%d -> " % (head.val), end = "")
        head = head.next
    print("NULL")

if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    head = Solution().sortList(node1)
    print_list(head)
