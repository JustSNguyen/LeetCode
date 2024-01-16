# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            min_val = root.val
            max_val = root.val
            if root.left:
                min_left, max_left, is_valid_left = dfs(root.left)
                if not is_valid_left or max_left >= root.val:
                    return -1, -1, False

                min_val = min_left

            if root.right:
                min_right, max_right, is_valid_right = dfs(root.right)
                if not is_valid_right or min_right <= root.val:
                    return -1, -1, False

                max_val = max_right

            return min_val, max_val, True

        return dfs(root)[2]