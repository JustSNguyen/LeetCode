from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None 

        def merge_sort_linked_list(start_node, end_node, number_of_nodes):
            if number_of_nodes == 1: 
                start_node.next = None 
                return start_node

            number_of_left_nodes  = number_of_nodes // 2 
            number_of_right_nodes = number_of_nodes - number_of_left_nodes
            cur_length = 1 
            cur_node = start_node

            while cur_length < number_of_left_nodes:
                cur_node = cur_node.next 
                cur_length += 1 

            middle_node = cur_node 
            start_of_right_head = middle_node.next

            left_head = merge_sort_linked_list(start_node, middle_node, number_of_left_nodes)
            right_head = merge_sort_linked_list(start_of_right_head, end_node, number_of_right_nodes)

            sorted_head = None 
            cur_node = None 
            while left_head or right_head: 
                if not left_head: 
                    cur_node.next = right_head 
                    right_head = right_head.next 
                    cur_node = cur_node.next 

                elif not right_head: 
                    cur_node.next = left_head 
                    left_head = left_head.next 
                    cur_node = cur_node.next 
                
                elif left_head.val < right_head.val: 
                    if not cur_node: 
                        cur_node = left_head 
                        sorted_head = left_head 
                    else:
                        cur_node.next = left_head 
                        cur_node = cur_node.next 

                    left_head = left_head.next 
                
                else: 
                    if not cur_node: 
                        cur_node = right_head 
                        sorted_head = right_head
                    else: 
                        cur_node.next = right_head
                        cur_node = cur_node.next 

                    right_head = right_head.next
            
            cur_node.next = None 

            return sorted_head

        number_of_nodes = 0 
        tail = None 
        cur_node = head 

        while cur_node: 
            number_of_nodes += 1 
            tail = cur_node 
            cur_node = cur_node.next 
        
        sorted_head = merge_sort_linked_list(head, tail, number_of_nodes)

        return sorted_head

if __name__ == "__main__": 
    node_1 = ListNode(4)
    node_2 = ListNode(2)
    node_3 = ListNode(1)
    node_4 = ListNode(3)

    node_1.next = node_2 
    node_2.next = node_3
    node_3.next = node_4 

    sol = Solution()
    new_head = sol.sortList(None)

    while new_head: 
        print(new_head.val, end = " ")

        new_head = new_head.next 
    