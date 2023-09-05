# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copy_linked_list_value_only(self, head):
        copy_of_node = dict()

        cur_node = head 
        while cur_node:
            copy_of_node[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next

        return copy_of_node


    def connect_copied_nodes(self, copy_of_node):
        for original_node in copy_of_node:
            copy_node = copy_of_node[original_node]

            if original_node.next:
                copy_node.next = copy_of_node[original_node.next]
            
            if original_node.random:
                copy_node.random = copy_of_node[original_node.random]


    def copyRandomList(self, head):
        if not head:
            return None

        copy_of_node = self.copy_linked_list_value_only(head)
        
        self.connect_copied_nodes(copy_of_node)

        return copy_of_node[head]
