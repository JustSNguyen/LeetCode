from collections import deque 

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root: 
            return root 

        nodes_seperated_by_levels = dict()
        level_of_node = dict()
        level_of_node[root] = 0 
        visited = dict()
        queue = deque()

        queue.append(root)

        while queue: 
            cur_node = queue.popleft()
            if cur_node in visited:
                return 
            
            visited[cur_node] = True 
            node_level = level_of_node[cur_node] 
            if node_level not in nodes_seperated_by_levels:
                nodes_seperated_by_levels[node_level] = []
            nodes_seperated_by_levels[node_level].append(cur_node)

            left_node = cur_node.left 
            right_node = cur_node.right 

            if left_node and left_node not in visited:
                level_of_node[left_node] = level_of_node[cur_node] + 1
                queue.append(left_node)
            
            if right_node and right_node not in visited:
                level_of_node[right_node] = level_of_node[cur_node] + 1 
                queue.append(right_node)
            
        for level in nodes_seperated_by_levels:
            prev = None 
            for node in nodes_seperated_by_levels[level]:
                if prev: 
                    prev.next = node 
                
                prev = node 
        
        return root 
    
            
