# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head 
        fast = head 
        new_head = None 
        prev_tail = None 

        while True:
            cnt = 0 
            while cnt != k and fast:
                fast = fast.next 
                cnt += 1 
            
            if cnt != k:
                break 

            first = None 
            prev = None 
            while slow != fast:
                if not first:
                    first = slow 

                next_slow = slow.next 
                slow.next = prev 
                prev = slow 
                slow = next_slow
            
            if prev_tail:
                prev_tail.next = prev 
            
            prev_tail = first

            if not new_head:
                new_head = prev 
            
            first.next = slow 
        
        return new_head 