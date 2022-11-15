# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ##my approach - very slow and takes more memory
        # def getitem(ll): ##get node value from both the list
        #     s = ""
        #     item_curr = ll
        #     while item_curr is not None:
        #         if s:
        #             s+=str(item_curr.val)
        #         else:
        #             s = str(item_curr.val)
        #         item_curr = item_curr.next
        #     return s
        # s1 = getitem(l1)[::-1] ##reverse the 2 strings
        # s2 = getitem(l2)[::-1]
        # s3 = int(s1) + int(s2)
        # s3 = list(str(s3)[::-1]) ##reverse the output string again as we add nodes to the output LL from behind
        # l3 = ListNode()
        # def addnode(ll): ##recursive function to keep adding all elements in a list to a linked list
        #     if len(ll)==1:
        #         return ListNode(val=ll[0])
        #     return ListNode(ll[0],addnode(ll[1:]))
        # l3 = addnode(s3)
        # return l3
        dummy = ListNode() ##create output LinkedList
        curr = dummy ##curr helps us track the current node in the output linkedlist
        carry = 0 ##important for edge case, we compute carry seperated
        while l1 or l2 or carry: ##keep looping as long as there is an element in either of the linkedlists or carry value is not 0
            v1 = l1.val if l1 else 0 #if l1 has node, v1 is its value
            v2 = l2.val if l2 else 0
            value = v1 + v2 + carry #final value to be inserted is sum of v1,v2, and carry as well. It might be 0 or 1, depending on previous nodes values
            carry = value//10 ##compute value of carry by divinding value by 10
            value = value%10 ##since node to be inserted can only be 1 digit
            curr.next = ListNode(value) ##insert computed value into output LL
            curr = curr.next
            l1 = l1.next if l1 else None ##l1 moves over if there are elements left
            l2 = l2.next if l2 else None ##same as above
        return dummy.next
            
            
            
            
            
            
        
        
        
        
        

        
        