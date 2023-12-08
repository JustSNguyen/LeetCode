from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_pos = {inorder[i]: i for i in range(len(inorder))}

        def build_recursively(start, end):
            if start > end:
                return None

            root = TreeNode(postorder[-1])

            postorder.pop()

            root.right = build_recursively(inorder_pos[root.val] + 1, end)
            root.left = build_recursively(start, inorder_pos[root.val] - 1)

            return root

        return build_recursively(0, len(inorder) - 1)

if __name__ == '__main__':
    sol = Solution()
    inorder = [2, 1]
    postorder = [2, 1]
    result = sol.buildTree(inorder, postorder)
