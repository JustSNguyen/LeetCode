from typing import List, Optional
from collections import deque 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_of_node = dict()
        visited = dict()
        level_of_node[root] = 1
        nodes_seperated_by_levels = dict()

        queue = deque()
        queue.append(root)

        while queue:
            cur_node = queue.popleft()

            if cur_node in visited:
                continue 

            visited[cur_node] = True 
            cur_level = level_of_node[cur_node]
            if cur_level not in nodes_seperated_by_levels:
                nodes_seperated_by_levels[cur_level] = []
            
            nodes_seperated_by_levels[cur_level].append(cur_node)

            left_node = cur_node.left 
            right_node = cur_node.right 
            if left_node and left_node not in visited:
                level_of_node[left_node] = level_of_node[cur_node] + 1 
                queue.append(left_node)
            
            if right_node and right_node not in visited:
                level_of_node[right_node] = level_of_node[cur_node] + 1 
                queue.append(right_node)
        
        zigzag_result = []
        for level in nodes_seperated_by_levels:
            cur_level_nodes = []
            start = 0 
            end = len(nodes_seperated_by_levels[level])
            step = 1 
            if level % 2 == 0:
                start = len(nodes_seperated_by_levels[level]) - 1 
                end = -1 
                step = -1 
            
            for i in range(start, end, step):
                cur_node = nodes_seperated_by_levels[level][i]
                cur_level_nodes.append(cur_node.val)
            
            zigzag_result.append(cur_level_nodes)
        
        return zigzag_result
    
if __name__ == "__main__":
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    # three.left = nine
    # three.right = twenty
    # twenty.left = fifteen 
    # twenty.right = seven 

    sol = Solution()
    result = sol.zigzagLevelOrder(three)

    print(result)

