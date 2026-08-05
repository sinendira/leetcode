# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findLengthOfLL(self, head):
        l = 0
        curr = head

        while curr:
            l += 1
            curr = curr.next
        return l
    def reversenodes(self, head, k, length):
        if length < k: return head

        curr = head
        prev = None
        nex = None
        count = 0
        while curr and count < k:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count += 1
        if nex:
            head.next = self.reversenodes(nex, k, length-k)

        return prev
        
    def reverseKGroup(self, head, k):
        length = self.findLengthOfLL(head)
        return self.reversenodes(head, k, length)
        