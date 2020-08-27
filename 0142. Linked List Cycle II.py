class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return None

        zcs = head
        slow = slow.next
        while zcs != slow:
            zcs = zcs.next
            slow = slow.next
        return zcs

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node4

    ret = Solution().detectCycle(node1)
    print(ret.val)