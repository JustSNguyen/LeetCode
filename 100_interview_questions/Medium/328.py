from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head 

        even_list_head = None 
        odd_list_tail = head 

        cur_index = 1 
        cur_node = head 
        last_odd_node = None 
        last_even_node = None 

        while cur_node:
            if cur_index % 2:
                if last_odd_node:
                    last_odd_node.next = cur_node 
                
                last_odd_node = cur_node 
                odd_list_tail = cur_node 
            else:
                if not last_even_node:
                    even_list_head = cur_node 
                else: 
                    last_even_node.next = cur_node 
                
                last_even_node = cur_node 
            
            cur_index += 1 
            cur_node = cur_node.next 

        if last_even_node:
            last_even_node.next = None 
        
        odd_list_tail.next = even_list_head 

        return head 

if __name__ == "__main__":
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    first.next = second 
    second.next = third 
    third.next = fourth 
    # fourth.next = fifth

    sol = Solution()
    new_head = sol.oddEvenList(first)

    print(new_head)

    cur = new_head 
    while cur: 
        print(cur.val, end = " ")
        cur = cur.next 

