# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, head: Optional['Node']) -> Optional['Node']:
        if not head:
            return None

        cloned = dict()

        def clone(node):
            copy_node = Node(node.val)
            cloned[node] = copy_node

            for neigh in node.neighbors:
                if neigh in cloned:
                    copy_node.neighbors.append(cloned[neigh])
                else:
                    cloned_neigh = clone(neigh)
                    copy_node.neighbors.append(cloned_neigh)

            return copy_node

        return clone(head)

if __name__ == '__main__':
    head = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    head.neighbors.extend([two, four])
    two.neighbors.extend([head, three])
    three.neighbors.extend([two, four])
    four.neighbors.extend([head, three])

    sol = Solution()
    result = sol.cloneGraph(head)
    print(result.val, result.neighbors)
