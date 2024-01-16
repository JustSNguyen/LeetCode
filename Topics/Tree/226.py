# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []

        if root:
            stack.append((None, 0, root))

        while stack:
            parent, is_currently_right, cur = stack.pop()
            if parent:
                if is_currently_right:
                    parent.left = cur
                else:
                    parent.right = cur

            if cur.left:
                stack.append((cur, 0, cur.left))
            if cur.right:
                stack.append((cur, 1, cur.right))

            cur.left = None
            cur.right = None

        return root