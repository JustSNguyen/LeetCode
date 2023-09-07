from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    cur_node = head 
    while cur_node:
        print(cur_node.val, end = "")
        if cur_node.next:
            print("->", end = "")
        cur_node = cur_node.next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        last_node_before_left = None 
        left_node = None 
        right_node = None  
        cur_node = head 
        prev_node = None 
        node_order = 0 

        while cur_node:
            next_node = cur_node.next 
            node_order += 1 

            if node_order < left:
                last_node_before_left = cur_node 

            if node_order == left:
                left_node = cur_node 
                left_node.next = None
            
            if node_order == right:
                right_node = cur_node

            if node_order == right + 1:
                left_node.next = cur_node
            
            if left < node_order <= right:
                cur_node.next = prev_node

            prev_node = cur_node
            cur_node = next_node

        if last_node_before_left:
            last_node_before_left.next = right_node
        else:
            head = right_node

        return head 

if __name__ == '__main__':
    node_5 = ListNode(5, None)
    node_4 = ListNode(4, node_5)
    node_3 = ListNode(3, node_4)
    node_2 = ListNode(2, node_3)
    node_1 = ListNode(1, node_2)
    sol = Solution()
    head = sol.reverseBetween(node_1, 1, 5)
    print_linked_list(head)