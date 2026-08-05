class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        #connect tail to head
        cur= head
        length =1
        while cur.next:
            cur = cur.next
            length+=1 
        cur.next = head

        #move to new head
        k= length - (k%length)
        while k>0:
            cur=cur.next
            k-=1

        #disconnect and return new head
        newhead = cur.next
        cur.next=None
        return newhead