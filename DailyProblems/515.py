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
        processed = set()

        queue.append((root, 0))

        while queue:
            node, row = queue.popleft()
            if node in processed:
                continue

            processed.add(node)

            if row >= len(max_value_at_row):
                max_value_at_row.append(node.val)
            else:
                max_value_at_row[row] = max(max_value_at_row[row], node.val)

            if node.left and node.left not in processed:
                queue.append((node.left, row + 1))
            if node.right and node.right not in processed:
                queue.append((node.right, row + 1))

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