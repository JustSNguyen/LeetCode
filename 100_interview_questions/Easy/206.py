from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse_list_iterative(head)

    def reverse_list_iterative(self, head):
        cur_node = head 
        prev_node = None 

        while cur_node:
            next_node = cur_node.next 
            cur_node.next = prev_node 
            prev_node = cur_node 
            cur_node = next_node 
        
        return prev_node
    
    def reverse_list_recursive(self, cur_node):
        if not cur_node: 
            return None, None 

        head, tail = self.reverse_list_recursive(cur_node.next)
        if not head:
            return cur_node, cur_node

        cur_node.next = None 
        tail.next = cur_node
        
        return head, cur_node

    
    def print_linked_list(self, head):
        cur_node = head 
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next 

    
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    head.next = two 
    two.next = three 
    three.next = four 
    four.next = five 

    new_head = sol.reverseList(head)
    sol.print_linked_list(new_head)


    
        