# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = defaultdict(lambda: [root for _ in range(20)])
        heights = dict()
        stack = []
        stack.append((root, 0))
        heights[root] = 0

        while stack:
            node, height = stack.pop()

            if node.left:
                heights[node.left] = height + 1

                parent[node.left][0] = node
                for i in range(1, 20):
                    parent[node.left][i] = parent[parent[node.left][i - 1]][i - 1]

                stack.append((node.left, heights[node.left]))

            if node.right:
                heights[node.right] = height + 1

                parent[node.right][0] = node
                for i in range(1, 20):
                    parent[node.right][i] = parent[parent[node.right][i - 1]][i - 1]

                stack.append((node.right, heights[node.right]))


        def jump(node, distance):
            if distance == 0:
                return node

            if distance == 1:
                return parent[node][0]

            cur = node
            for i in range(19, -1 , -1):
                jump_distance = (1 << i)
                if jump_distance > distance: continue

                cur = parent[cur][i]
                distance -= jump_distance

            return cur

        if heights[p] < heights[q]:
            p, q = q, p

        p = jump(p, heights[p] - heights[q])

        if p == q:
            return p

        for i in range(19, -1, -1):
            if parent[p][i] == parent[q][i]: continue
            p = parent[p][i]
            q = parent[q][i]

        return parent[p][0]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2)
    one = TreeNode(1)
    root.left = one
    #
    # two = TreeNode(2)
    # eight = TreeNode(8)
    #
    # zero = TreeNode(0)
    # four = TreeNode(4)
    # seven = TreeNode(7)
    # nine = TreeNode(9)
    #
    # three = TreeNode(3)
    # five = TreeNode(5)
    #
    # two.left = zero
    # two.right = four
    #
    # eight.left = seven
    # eight.right = nine
    #
    # four.left = three
    # four.right = five
    #
    # root.left = two
    # root.right = eight

    p = root
    q = one

    result = sol.lowestCommonAncestor(root, p, q)
    print(result.val)