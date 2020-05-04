class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        first = ListNode(0)
        first.next = head
        e = head
        n = head.next
        while n is not None:
            e.next = n.next
            n.next = None

            zcs = first
            # print_list(first)
            while zcs != e and zcs.next.val < n.val:
                zcs = zcs.next
            if zcs == e:
                n.next = e.next
                e.next = n
                e = n
            else:
                n.next = zcs.next
                zcs.next = n
            n = e.next
        return first.next

def print_list(head):
    while head is not None:
        print("%d -> " % (head.val), end = "")
        head = head.next
    print("NULL")

if __name__ == "__main__":
    # node1 = ListNode(-1)
    # node2 = ListNode(5)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(0)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    head = Solution().insertionSortList(node1)
    print_list(head)