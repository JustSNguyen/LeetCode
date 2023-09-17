from typing import List
from collections import deque
from functools import lru_cache

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        number_of_nodes = len(graph)

        def get_ith_bit(num, i):
            bit = (num >> i) & 1
            return bit

        def set_ith_bit(num, i):
            # Left shift 1 by i positions to create a mask with only the ith bit set to 1
            mask = 1 << i
            # Use bitwise OR to set the ith bit to 1 in the original number
            result = num | mask
            return result

        def calculate_shortest_paths_start_from(node_index):
            queue = deque()
            visited = [False for _ in range(number_of_nodes)]
            dist = [number_of_nodes for _ in range(number_of_nodes)]
            dist[node_index] = 0
            queue.append(node_index)
            while queue:
                cur_node_index = queue.popleft()
                if visited[cur_node_index]:
                    continue
                visited[cur_node_index] = True

                for neighbor in graph[cur_node_index]:
                    if visited[neighbor]:
                        continue

                    dist[neighbor] = min(dist[neighbor], dist[cur_node_index] + 1)
                    queue.append(neighbor)

            return dist

        @lru_cache(maxsize = 10**6)
        def get_shortest_path(node_index, visited):
            min_total_dist = 10**12

            all_visited = True
            for other_node in range(number_of_nodes):
                if get_ith_bit(visited, other_node) == 1:
                    continue

                all_visited = False
                new_visited = set_ith_bit(visited, other_node)
                min_total_dist = min(min_total_dist, dist[node_index][other_node] + get_shortest_path(other_node,
                                                                                                    new_visited))

            if all_visited:
                return 0

            return min_total_dist

        dist = []
        for i in range(number_of_nodes):
            dist.append(calculate_shortest_paths_start_from(i))

        shortest_path = 10**12
        for i in range(number_of_nodes):
            visited = set_ith_bit(0, i)
            shortest_path = min(shortest_path, get_shortest_path(i, visited))

        return shortest_path

if __name__ == '__main__':
    sol = Solution()
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    result = sol.shortestPathLength(graph)
    print(result)