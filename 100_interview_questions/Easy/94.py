from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_traverse_helper(node, result):
            if not node: 
                return None 
            
            in_order_traverse_helper(node.left, result)
            result.append(node.val)
            in_order_traverse_helper(node.right, result)
        
        result = []
        in_order_traverse_helper(root, result)

        return result 
    
if __name__ == '__main__':
    root = TreeNode(1)
    node_1 = TreeNode(2)
    node_2 = TreeNode(3)
    root.right = node_1 
    node_1.left = node_2 

    sol = Solution()
    result = sol.inorderTraversal(root)
    print(result)
            