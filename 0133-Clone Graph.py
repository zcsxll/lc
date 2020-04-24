# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

import queue

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        q = queue.Queue() #广度优先遍历
        q.put(node)
        
        all_nodes = {} #字典中的node是被复制的新节点
        all_nodes[node.val] = Node(node.val)

        while not q.empty():
            cur_node = q.get()
            print("get %d" % cur_node.val) #打印没有影响，但估计会影响时间
            for neighbor in cur_node.neighbors:
                if neighbor.val not in all_nodes.keys():
                    all_nodes[neighbor.val] = Node(neighbor.val)
                    q.put(neighbor)
                    print("put %d" % neighbor.val)
                all_nodes[cur_node.val].neighbors.append(all_nodes[neighbor.val])
        return all_nodes[node.val]


if __name__ == "__main__":
    node1 = Node(1, ((2, 4)))
    node2 = Node(2, (1, 3))
    node3 = Node(3, (2, 4))
    node4 = Node(4, (1, 3))
    node1.neighbors = (node2, node4)
    node2.neighbors = (node1, node3)
    node3.neighbors = (node2, node4)
    node4.neighbors = (node1, node3)
    ret = Solution().cloneGraph(node1)
    print(ret)