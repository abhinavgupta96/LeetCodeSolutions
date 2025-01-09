"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def flatten_list(prevNode, currentNode):
            if currentNode is None:
                return prevNode

            nextNode = currentNode.next
            prevNode.next = currentNode
            currentNode.prev = prevNode

            tailList = flatten_list(currentNode, currentNode.child)
            currentNode.child = None
            return flatten_list(tailList, nextNode)
        if head is None:
            return None

        dummy = Node(0)
        flatten_list(dummy, head)
        dummy.next.prev = None
        return dummy.next
