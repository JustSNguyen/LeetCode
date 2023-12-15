from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst_recursive(root):
            cur_max_node = root.val
            cur_min_node = root.val
            if root.left:
                is_valid, max_node, min_node = is_valid_bst_recursive(root.left)
                if not is_valid or root.val <= max_node:
                    return False, -1, -1

                cur_min_node = min_node

            if root.right:
                is_valid, max_node, min_node = is_valid_bst_recursive(root.right)
                if not is_valid or root.val >= min_node:
                    return False, -1, -1

                cur_max_node = max_node

            return True, cur_max_node, cur_min_node

        return is_valid_bst_recursive(root)[0]