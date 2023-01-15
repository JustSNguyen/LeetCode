from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = head1 
        prev = None 
        head = None 
        while head1 != None or head2 != None:
            next_node = None 
            if not head1: 
                next_node = head2
                head2 = head2.next
            elif not head2: 
                next_node = head1 
                head1 = head1.next 
            elif head1.val < head2.val: 
                next_node = head1 
                head1 = head1.next 
            else: 
                next_node = head2 
                head2 = head2.next 
            
            if not head: 
                head = next_node 
            
            if not prev:
                prev = head 
            else: 
                prev.next = next_node 
                prev = next_node

        return head 
    
            