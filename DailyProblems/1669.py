# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = None
        prev = None
        i = 0

        while list1:
            if i == a:
                while i <= b and list1:
                    list1 = list1.next
                    i += 1

                while list2:
                    if prev:
                        prev.next = list2
                    else:
                        head = list2

                    prev = list2
                    list2 = list2.next
            else:
                i += 1
                if prev:
                    prev.next = list1
                else:
                    head = list1

                prev = list1
                list1 = list1.next

        return head



