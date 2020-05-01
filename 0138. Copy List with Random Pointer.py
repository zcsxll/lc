# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def print_list(head):
    node = head
    while node is not None:
        random = node.random
        zcs = -1 if random is None else random.val
        print("[%d, %d]" % (node.val, zcs), end = " ")
        node = node.next
    print()

class Solution:
    """
    解法2：
    复制head为new_head（next和random指针也一样）并把new_head放入list，还要记录dict[head]=new_head
    取出list队首节点，如果节点的next不为空，则查找dict中是否有next，没有则复制一下放入list后边，并在dict中记录dict[next]=new_next
    然后修改刚刚取出的节点的next=new_next
    刚刚取出的节点的random，做一样的处理
    直到list为空
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        node = head
        while node is not None: #第一次遍历，复制每个节点插在原链表的后边
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next
        node = head
        while node is not None: #第二次遍历，处理random指针
            if node.random is not None:
                node.next.random = node.random.next
            node = node.next.next
        # print_list(head)
        node = head
        ret_head = head.next
        while node is not None and node.next.next is not None: #第三次遍历，拆出复制的链表
            tmp1 = node.next
            tmp2 = node.next.next.next
            node = node.next.next
            tmp1.next = tmp2
        return ret_head

if __name__ == "__main__":
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node1.random = node3
    node2.next = node3
    node3.random = node1
    print_list(node1)
    ret = Solution().copyRandomList(node1)
    print_list(ret)