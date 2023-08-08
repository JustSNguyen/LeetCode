from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traverse(root, result):
            if not root:
                return 
            
            inorder_traverse(root.left, result)
            result.append(root.val)
            inorder_traverse(root.right, result)

            return result 

        inorder_traverse_result = inorder_traverse(root, [])
        return inorder_traverse_result[k - 1]

if __name__ == '__main__':
    root = TreeNode(3)
    one_node = TreeNode(1)
    two_node = TreeNode(2)
    four_node = TreeNode(4)
    one_node.right = two_node
    root.left = one_node 
    root.right = four_node
    
    sol = Solution()
    print(sol.kthSmallest(root, 1))

