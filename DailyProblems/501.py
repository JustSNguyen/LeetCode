from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.previous_node = None
        self.count = 0
        self.max_count = 0
        self.found_max_count = False
        self.modes = dict()
        def in_order_traversal(root):
            if root.left:
                in_order_traversal(root.left)

            if not self.previous_node or self.previous_node.val != root.val:
                self.count = 1
            else:
                self.count += 1
            self.previous_node = root

            self.max_count = max(self.max_count, self.count)
            if self.found_max_count and self.count == self.max_count:
                self.modes[root.val] = 1

            if root.right:
                in_order_traversal(root.right)

        in_order_traversal(root)
        self.found_max_count = True
        in_order_traversal(root)

        return list(self.modes.keys())



