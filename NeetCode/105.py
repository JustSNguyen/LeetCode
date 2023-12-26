

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_in_inorder = {inorder[i]: i for i in range(len(inorder))}

        preorder = deque(preorder)
        def build_recursively(i, j):
            if i > j:
                return None

            root_value = preorder.popleft()
            root = TreeNode(root_value)

            root_index_in_inorder = index_in_inorder[root_value]

            root.left = build_recursively(i, root_index_in_inorder - 1)
            root.right = build_recursively(root_index_in_inorder + 1, j)

            return root

        return build_recursively(0, len(preorder) - 1)

if __name__ == "__main__":
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    result = sol.buildTree(preorder, inorder)
    print(result)
