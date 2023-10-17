from typing import List
from collections import defaultdict

class Solution:
    def validateBinaryTreeNodes(self, n: int, left_child: List[int], right_child: List[int]) -> bool:
        neighbors = [[] for _ in range(n)]
        def graph_has_cycle(cur_node, colors):
            if colors[cur_node] == 2:
                return False

            if colors[cur_node] == 1:
                return True

            colors[cur_node] = 1
            has_cycle = False
            for neighbor in neighbors[cur_node]:
                if graph_has_cycle(neighbor, colors):
                    has_cycle = True

            colors[cur_node] = 2
            return has_cycle

        number_of_children = defaultdict(int)
        number_of_parents = defaultdict(int)

        for i in range(n):
            if left_child[i] != -1:
                neighbors[i].append(left_child[i])
                number_of_children[i] += 1

                number_of_parents[left_child[i]] += 1
                if number_of_parents[left_child[i]] > 1:
                    return False

            if right_child[i] != -1:
                neighbors[i].append(right_child[i])
                number_of_children[i] += 1

                number_of_parents[right_child[i]] += 1
                if number_of_parents[right_child[i]] > 1:
                    return False

            if number_of_children[i] > 2:
                return False

        head_node = 0
        for node in range(n):
            if number_of_parents[node] == 0:
                head_node = node

        colors = {node: 0 for node in range(n)}
        if graph_has_cycle(head_node, colors):
            return False

        number_of_nodes_processed = 0
        for node in range(n):
            if colors[node] == 2:
                number_of_nodes_processed += 1

        return number_of_nodes_processed == n

if __name__ == '__main__':
    sol = Solution()
    n = 2
    leftChild = [-1, -1]
    rightChild = [-1,-1]
    result = sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    print(result)
