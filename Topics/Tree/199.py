# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        q = deque()

        if root:
            q.append((root, 1))

        while q:
            node, level = q.popleft()

            if level > len(right_side_view):
                right_side_view.append(node.val)
            else:
                right_side_view[level - 1] = node.val

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return right_side_view