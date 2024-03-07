class Solution:
    def middleNode(self, h: Optional[ListNode]) -> Optional[ListNode]:
        f = h
        while f and f.next:
            h, f = h.next, f.next.next
        return h
        