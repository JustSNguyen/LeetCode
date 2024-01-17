# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -math.pow(10, 12)

        def dfs(root):
            if not root:
                return 0

            max_left = max(0, dfs(root.left))
            max_right = max(0, dfs(root.right))

            new_path_sum = root.val + max_right + max_left
            self.max_path_sum = max(self.max_path_sum, new_path_sum)

            return max(max_left, max_right) + root.val

        dfs(root)
        return self.max_path_sum