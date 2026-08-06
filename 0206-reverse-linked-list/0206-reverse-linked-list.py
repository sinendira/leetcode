"""
Array

Time: O(N) where N = total # of nodes in linked list
Iterate through linked list
Space: O(N)
nodes array
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Put each node in an array
        nodes = []
        curr = head
        while curr != None:
            nodes.append(curr)
            curr = curr.next
        
        if len(nodes) == 0:
            return None
        
        # Iterate through list in reverse and reform the connections
        N = len(nodes)
        for idx in range(N, 0, -1):
            nodes[idx-1].next = nodes[idx-2]

        # Last node set its next to null
        nodes[0].next = None
    
        return nodes[-1]