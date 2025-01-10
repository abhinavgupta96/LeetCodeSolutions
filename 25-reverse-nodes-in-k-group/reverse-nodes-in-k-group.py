# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            start = groupPrev.next
            reverse(start, group_next)

            groupPrev.next = kth
            start.next = group_next

            groupPrev = start
