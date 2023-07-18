from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert_sorted_array_bst(left, right):
            if right < left: return None 

            number_of_elements = right -left + 1;
            cur_root = None 
            if number_of_elements == 1:
                cur_root = TreeNode(val = nums[left]) 
            
            else: 
                middle_element = left + (right - left) // 2  
                cur_root = TreeNode(val = nums[middle_element])
                cur_root.left = convert_sorted_array_bst(left, middle_element - 1) 
                cur_root.right = convert_sorted_array_bst(middle_element + 1, right)
            
            return cur_root

        return convert_sorted_array_bst(0, len(nums) - 1)
    

def print_tree(root):
    queue = deque()
    visited = dict()

    queue.append(root)

    while queue:
        cur_node = queue.popleft()
        print(cur_node.val)
        if cur_node in visited:
            continue 

        visited[cur_node] = True 

        if cur_node.left and cur_node.left not in visited:
            queue.append(cur_node.left) 
        
        if cur_node.right and cur_node.right not in visited:
            queue.append(cur_node.right)

if __name__ == "__main__":
    sol = Solution()
    nums = [1]
    root = sol.sortedArrayToBST(nums)
    print_tree(root)