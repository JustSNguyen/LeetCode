from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_parent = dict()
        node_rank = dict()
        
        node_parent[root] = None 
        node_rank[root] = 0 

        queue  = deque()
        queue.append(root)
        while queue: 
            cur_node = queue.popleft()

            if cur_node.left:
                node_parent[cur_node.left] = cur_node 
                node_rank[cur_node.left] = node_rank[cur_node] + 1
                queue.append(cur_node.left)
            
            if cur_node.right:
                node_parent[cur_node.right] = cur_node 
                node_rank[cur_node.right] = node_rank[cur_node] + 1 
                queue.append(cur_node.right)
        
        while p != q:
            if node_rank[p] > node_rank[q]:
                p = node_parent[p]
            
            elif node_rank[q] > node_rank[p]:
                q = node_parent[q]
            
            else: 
                q = node_parent[q]
                p = node_parent[p]
        
        return p 

if __name__ == "__main__":
    root = TreeNode(3)
    five = TreeNode(5)
    one = TreeNode(1)
    six = TreeNode(6)
    two = TreeNode(2)
    zero = TreeNode(0)
    eight = TreeNode(8)
    seven = TreeNode(7)
    four = TreeNode(4)

    root.left = five 
    root.right = one  

    five.left = six
    five.right = two 

    one.left = zero 
    one.right = eight 

    two.left = seven
    two.right = four 

    sol = Solution()
    result = sol.lowestCommonAncestor(root, six, zero)

    print(result.val)