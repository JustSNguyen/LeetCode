from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        max_value_at_row = []
        queue = deque()
        queue.append(root)

        while queue:
            max_value = queue[0].val
            number_of_nodes_left = len(queue)

            while number_of_nodes_left > 0:
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                number_of_nodes_left -= 1

            max_value_at_row.append(max_value)

        return max_value_at_row


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    three_1 = TreeNode(3)
    two_1 = TreeNode(2)
    five_2 = TreeNode(5)
    three_2 = TreeNode(3)
    nine_2 = TreeNode(9)

    root.left = three_1
    root.right = two_1

    # three_1.left = five_2
    # three_1.right = three_2
    #
    # two_1.right = nine_2

    result = s.largestValues(root)
    print(result)