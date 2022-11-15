# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getitem(ll):
            s = ""
            item_curr = ll
            while item_curr is not None:
                if s:
                    s+=str(item_curr.val)
                else:
                    s = str(item_curr.val)
                item_curr = item_curr.next
            return s
        s1 = getitem(l1)[::-1]
        s2 = getitem(l2)[::-1]
        s3 = int(s1) + int(s2)
        s3 = list(str(s3)[::-1])
        l3 = ListNode()
        def addnode(ll):
            if len(ll)==1:
                return ListNode(val=ll[0])
            return ListNode(ll[0],addnode(ll[1:]))
        l3 = addnode(s3)
        return l3

        
        