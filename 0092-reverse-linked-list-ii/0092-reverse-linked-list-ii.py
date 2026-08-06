class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:          # base case
            return head
        temp = ListNode(val=-1e9)
        temp.next = head
        curr = temp
        for _ in range(left - 1):               # iterate through the list
            curr = curr.next
            
            
        temp_curr = curr.next
        for _ in range(right - left):           # reverse the list
            nxt = temp_curr.next
            temp_curr.next = nxt.next
            nxt.next = curr.next
            curr.next = nxt

        return temp.next