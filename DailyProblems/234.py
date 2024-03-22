# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True 
        

        prev_slow = None 
        slow = head 
        fast = head 
        while fast and fast.next:
            prev_slow = slow 
            slow = slow.next 
            fast = fast.next.next 
        
        
        mid = slow 
        prev_slow = None
        while slow:
            next_slow = slow.next 
            slow.next = prev_slow 
            prev_slow = slow 
            slow = next_slow 
        
        tail = prev_slow 
        
        while head != mid:
            if head.val != tail.val:
                return False 
            
            head = head.next 
            tail = tail.next 
        
        return True 
        
