from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result_list = [f"{root.val}"]
        if root.left:
            result_list.append("(")
            result_list.append(self.tree2str(root.left))
            result_list.append(")")

        if root.right:
            if not root.left:
                result_list.append("()")

            result_list.append("(")
            result_list.append(self.tree2str(root.right))
            result_list.append(")")

        return "".join(result_list)


if __name__ == '__main__':
    sol = Solution()
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)

    two.right = four
    one.left = two
    one.right = three

    result = sol.tree2str(one)
    print(result)
