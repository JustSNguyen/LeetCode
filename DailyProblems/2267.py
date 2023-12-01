from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Response:
    def __init__(self, number_of_nodes: int, sum_nodes: int, number_of_qualified_nodes: int):
        self.number_of_nodes = number_of_nodes
        self.sum_nodes = sum_nodes
        self.number_of_qualified_nodes = number_of_qualified_nodes


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def get_subtree_response(root: TreeNode) -> Response:
            sum_nodes = root.val
            number_of_nodes = 1
            number_of_qualified_nodes = 0

            if root.left:
                left_response = get_subtree_response(root.left)
                sum_nodes += left_response.sum_nodes
                number_of_nodes += left_response.number_of_nodes
                number_of_qualified_nodes += left_response.number_of_qualified_nodes

            if root.right:
                right_response = get_subtree_response(root.right)
                sum_nodes += right_response.sum_nodes
                number_of_nodes += right_response.number_of_nodes
                number_of_qualified_nodes += right_response.number_of_qualified_nodes

            average = sum_nodes // number_of_nodes
            if average == root.val:
                number_of_qualified_nodes += 1

            return Response(number_of_nodes, sum_nodes, number_of_qualified_nodes)

        if not root:
            return 0

        return get_subtree_response(root).number_of_qualified_nodes
