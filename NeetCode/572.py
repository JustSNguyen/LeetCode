# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        self.distinct_trees = 0
        self.trees = dict()
        def generate_id(root):
            if not root:
                return -1

            left_id = generate_id(root.left)
            right_id = generate_id(root.right)
            tree = (left_id, root.val, right_id)
            if tree not in self.trees:
                self.trees[tree] = self.distinct_trees
                self.distinct_trees += 1

            return self.trees[tree]

        generate_id(root)
        original_tree_length = len(self.trees)

        generate_id(sub_root)
        new_tree_length = len(self.trees)

        return original_tree_length == new_tree_length

