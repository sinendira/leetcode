"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val)
            curr.next.next = nxt
            curr = nxt

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            copy = curr.next
            nxt = copy.next

            copy_curr.next = copy
            copy_curr = copy

            curr.next = nxt
            curr = nxt

        return dummy.next