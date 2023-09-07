from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_number_of_nodes_in_linked_list(self, head):
        number_of_nodes = 0 
        cur_node = head 
        while cur_node != None:
            number_of_nodes += 1 
            cur_node = cur_node.next 
        
        return number_of_nodes
    
    def print_linked_list(self, head):
        cur_node = head 
        while cur_node:
            print(cur_node.val, end = "")
            if cur_node.next:
                print(" -> ", end = "")

            cur_node = cur_node.next

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        number_of_nodes = self.get_number_of_nodes_in_linked_list(head)        
        number_of_groups_with_max_nodes = number_of_nodes % k 
        if number_of_groups_with_max_nodes == 0:
            number_of_groups_with_max_nodes = k
        max_nodes_per_group = (number_of_nodes + k - number_of_groups_with_max_nodes) // k 
        cur_expected_nodes_per_group = max_nodes_per_group

        result = []
        cur_node = head 
        cur_group = []
        while cur_node:
            next_node = cur_node.next 
            cur_group.append(cur_node)

            if len(cur_group) == cur_expected_nodes_per_group:
                last_node_in_group = cur_group[-1]
                last_node_in_group.next = None 
                
                head_of_group = cur_group[0]
                result.append(head_of_group)
                cur_group = []
            
            if len(result) == number_of_groups_with_max_nodes and cur_expected_nodes_per_group == max_nodes_per_group:
                cur_expected_nodes_per_group -= 1 
            
            cur_node = next_node 
        
        while len(result) < k:
            result.append(None)

        return result

if __name__ == '__main__':
    sol = Solution()
    node_10 = ListNode(10)
    node_9 = ListNode(9, node_10)
    node_8 = ListNode(8, node_9)
    node_7 = ListNode(7, node_8)
    node_6 = ListNode(6, node_7)
    node_5 = ListNode(5, node_6)
    node_4 = ListNode(4, node_5)
    node_3 = ListNode(3, None)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, None)
    head = node_1 
    k = 1

    sol.splitListToParts(None, k)