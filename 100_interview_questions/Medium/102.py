from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal_result = []

        if not root: 
            return traversal_result

        bfs_queue = deque()
        bfs_queue.append(root)
        processed = dict()
        level_of_node = dict()
        level_of_node[root] = 1

        while bfs_queue:
            node = bfs_queue.popleft()

            if node in processed:
                continue 

            processed[node] = True 

            node_level = level_of_node[node]
            if node_level > len(traversal_result):
                traversal_result.append([])
            
            traversal_result[node_level - 1].append(node.val)

            if node.left and node.left not in level_of_node:
                level_of_node[node.left] = level_of_node[node] + 1
                bfs_queue.append(node.left)
            
            if node.right and node.right not in level_of_node:
                level_of_node[node.right] = level_of_node[node] + 1
                bfs_queue.append(node.right)
            
        return traversal_result 
    
if __name__ == '__main__':
    root = TreeNode(1)
    sol = Solution()
    result = sol.levelOrder(root)
    print(result)
        
