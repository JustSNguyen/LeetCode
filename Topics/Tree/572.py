# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree_by_id = dict()

        def get_tree_id(root):
            if not root:
                return -1

            left_tree_id = get_tree_id(root.left)
            right_tree_id = get_tree_id(root.right)

            if (left_tree_id, root.val, right_tree_id) in tree_by_id:
                return tree_by_id[(left_tree_id, root.val, right_tree_id)]

            tree_by_id[(left_tree_id, root.val, right_tree_id)] = len(tree_by_id)
            return tree_by_id[(left_tree_id, root.val, right_tree_id)]

        get_tree_id(root)

        current_number_of_trees = len(tree_by_id)

        if get_tree_id(subRoot) < current_number_of_trees:
            return True

        return False

if __name__ == '__main__':
    sol = Solution()
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    one = TreeNode(1)
    two = TreeNode(2)
    zero = TreeNode(0)

    four.left = one
    four.right = two
    two.left = zero
    three.left = four
    three.right = five

    four2 = TreeNode(4)
    one2 = TreeNode(1)
    two2 = TreeNode(2)
    four2.left = one2
    four2.right = two2

    sol = Solution()
    result = sol.isSubtree(three, four2)
    print(result)
