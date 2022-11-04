# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,curr = dummy,head
        while curr and curr.next:
            ##saving pointer information
            second = curr.next
            nxtPair = curr.next.next
            second.next = curr
            ##swap next
            curr.next = nxtPair
            prev.next = second
            #shift pointers
            prev = curr
            curr = nxtPair
        return dummy.next
        