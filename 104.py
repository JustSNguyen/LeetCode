# Definition for a binary tree node.
from typing import DefaultDict, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        stack = []
        stack.append((root, 1))
        visited = dict()

        max_depth = 1

        while stack:
            node, cur_depth = stack.pop()
            max_depth = max(max_depth, cur_depth)

            if node in visited:
                continue 

            visited[node] = 1 

            if node.right: 
                stack.append((node.right, cur_depth + 1))

            if node.left:
                stack.append((node.left, cur_depth + 1))

        return max_depth