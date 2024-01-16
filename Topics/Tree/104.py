# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_height = 0
        stack = []

        if root:
            stack.append((root, 1))

        while stack:
            cur, height = stack.pop()
            max_height = max(max_height, height)

            if cur.left:
                stack.append((cur.left, height + 1))
            if cur.right:
                stack.append((cur.right, height + 1))

        return max_height