# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import defaultdict
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        adj = defaultdict(list)
        def find_max_length(start):
            max_length_from_start = -1
            node_with_max_length = None
            stack = []
            processed = set()

            if start:
                stack.append((start, 0))

            while stack:
                cur, length_from_start = stack.pop()

                if cur in processed:
                    continue

                processed.add(cur)

                if length_from_start > max_length_from_start:
                    node_with_max_length = cur
                    max_length_from_start = length_from_start

                if cur.left:
                    adj[cur].append(cur.left)
                    adj[cur.left].append(cur)
                if cur.right:
                    adj[cur].append(cur.right)
                    adj[cur.right].append(cur)

                for neighbor in adj[cur]:
                    if neighbor not in processed:
                        stack.append((neighbor, length_from_start + 1))

            return node_with_max_length, max_length_from_start

        node1, _ = find_max_length(root)
        _, diameter = find_max_length(node1)

        return diameter

if __name__ == '__main__':
    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    root.left = two
    root.right = three

    two.left = four
    two.right = five

    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    print(result)