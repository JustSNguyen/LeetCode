# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def is_balanced_recursive(root):
            if not root:
                return True, 0

            is_left_tree_balanced, left_tree_max_height = is_balanced_recursive(root.left)
            is_right_tree_balanced, right_tree_max_height = is_balanced_recursive(root.right)
            diff = abs(left_tree_max_height - right_tree_max_height)

            if is_right_tree_balanced and is_left_tree_balanced and diff <= 1:
                return True, max(left_tree_max_height, right_tree_max_height) + 1

            return False, -1

        return is_balanced_recursive(root)[0]
