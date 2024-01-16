# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        result = []

        if root:
            q.append((root, 1))

        while q:
            cur, level = q.popleft()
            if level > len(result):
                result.append([cur.val])
            else:
                result[level - 1].append(cur.val)

            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))

        return result