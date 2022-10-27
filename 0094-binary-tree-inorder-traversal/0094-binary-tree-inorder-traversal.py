# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_ll,inorder_st = [],[]
        if root is None:
            return inorder_ll
        temp = root
        while True:
            if temp:
                inorder_st.append(temp)
                temp = temp.left
            elif inorder_st:
                temp = inorder_st.pop()
                inorder_ll.append(temp.val)
                temp = temp.right
            else:
                break
        return inorder_ll
            
        
        