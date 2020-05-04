class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map.keys():
            node = self.map[key]
            self.move_to_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.map[key].val = value
            self.move_to_tail(self.map[key])
            return

        if len(self.map) >= self.capacity:
            self.map.pop(self.head.key)
            self.remove_head()
        node = self.append_node(key, value)
        self.map[key] = node

    def append_node(self, key, val):
        if self.head is None:
            self.head = Node(key, val)
            self.tail = self.head
            return self.head
        node = Node(key, val)
        node.pre = self.tail
        self.tail.next = node
        self.tail = node
        return node
    
    def remove_head(self):
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.pre = None

    def move_to_tail(self, node):
        if node.next is None:
            return
        if node.pre is None:
            self.head = self.head.next
            node.next.pre = None
            node.next = None
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

def print_list(head):
    while head is not None:
        print("%d:%d -> " % (head.key, head.val), end = "")
        head = head.next
    print("NULL")

if __name__ == "__main__":
    # cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1))#;       // returns 1
    # cache.put(3, 3)#;    // evicts key 2
    # print(cache.get(2))#;       // returns -1 (not found)
    # cache.put(4, 4)#;    // evicts key 1
    # print(cache.get(1))#;       // returns -1 (not found)
    # print(cache.get(3))#;       // returns 3
    # print(cache.get(4))#;       // returns 4

    # cache.put(2, 1)
    # cache.put(1, 2)
    # cache.put(2, 3)
    # cache.put(4, 1)
    # print(cache.get(1))
    # print(cache.get(2))

    action = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    param = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    cache = None
    cnt = 0
    for a, p in zip(action, param):
        print(a, p)
        if a == "LRUCache":
            cache = LRUCache(p[0])
        elif a == "put":
            cache.put(p[0], p[1])
            print_list(cache.head)
        else:
            value = cache.get(p[0])
            print(value)
            print_list(cache.head)
        cnt += 1
        if cnt >= 13:
            break