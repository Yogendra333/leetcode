# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        start = head
        cnt = 1
        while head.next:
            cnt+=1
            head = head.next
        head.next = start  #make list circular
        copy = ListNode(-1)
        ans = copy
        k%=cnt  # for large value of k
        for i in range(cnt-k):
            start = start.next
        for i in range(cnt):
            copy.next = start
            copy,start = copy.next,start.next
        copy.next = None  #break the circular linked list
        return ans.next
        