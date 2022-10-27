# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_ll = []
        preorder_st = []
        if root is None:
            return preorder_ll
        temp = root
        while True:
            if temp:
                preorder_st.append(temp)
                preorder_ll.append(temp.val)
                temp = temp.left
            elif preorder_st:
                temp = preorder_st.pop()
                temp = temp.right
            else:
                break
        return preorder_ll
        