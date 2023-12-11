from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        id_of_subtree = dict()
        self.unique_ids = 0

        def convert_trees_to_ids(root):
            if not root:
                return -1

            subtree = (convert_trees_to_ids(root.left), convert_trees_to_ids(root.right), root.val)

            if subtree not in subtrees:
                id_of_subtree[subtree] = self.unique_ids
                self.unique_ids += 1

            subtrees[subtree].append(root)

            return id_of_subtree[subtree]

        convert_trees_to_ids(root)

        result = [subtree[0] for subtree in subtrees.values() if len(subtree) > 1]

        return result




