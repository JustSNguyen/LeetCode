from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = [str(root.val)]

        if root.left or root.right:
            if root.left:
                result.append("(")
                result.append(self.tree2str(root.left))
                result.append(")")
            else:
                result.append("()")

            if root.right:
                result.append("(")
                result.append(self.tree2str(root.right))
                result.append(")")

        return "".join(result)