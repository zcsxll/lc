# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(vals):
    if len(vals) == 0:
        return None
    head = ListNode(vals[0])
    zcs = head
    for v in vals[1:]:
        zcs.next = ListNode(v)
        zcs = zcs.next
    return head

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        if mid.next is None:
            return
        print(mid.val)
        zcs = self.reverse(slow.next)
        slow.next = None

        n1 = head
        while zcs is not None:
            tmp1 = n1.next
            tmp2 = zcs.next
            n1.next = zcs
            zcs.next = tmp1
            zcs = tmp2
            n1 = tmp1

    def reverse(self, head):
        n1 = None
        n2 = head
        n3 = head.next
        while True:
            n2.next = n1
            n1 = n2
            n2 = n3
            if n2 is None:
                break
            n3 = n3.next
        return n1

if __name__ == "__main__":
    head = make_list([1, 2, 3, 4, 5, 6, 7, 8])
    Solution().reorderList(head)
    while head is not None:
        print(head.val, end = " ")
        head = head.next