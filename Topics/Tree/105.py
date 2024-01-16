# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {inorder[i]: i for i in range(len(inorder))}
        self.preorder_index = 0

        def build_recursively(left, right):
            if left > right:
                return None

            root_val = preorder[self.preorder_index]
            self.preorder_index += 1

            root = TreeNode(root_val)

            root.left = build_recursively(left, index_of[root.val] - 1)
            root.right = build_recursively(index_of[root.val] + 1, right)

            return root

        return build_recursively(0, len(preorder) - 1)



