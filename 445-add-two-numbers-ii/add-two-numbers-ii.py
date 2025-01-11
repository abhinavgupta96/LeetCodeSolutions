# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        carry = 0
        while l1 : 
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        dummy = ListNode()
        while s1 or s2 or carry:
            sum1 = s1.pop() if s1 else 0
            sum2 = s2.pop() if s2 else 0
            total = sum1 + sum2 + carry
            carry, curr = divmod(total, 10)

            node = ListNode(curr, dummy.next)
            dummy.next = node
        return dummy.next

        