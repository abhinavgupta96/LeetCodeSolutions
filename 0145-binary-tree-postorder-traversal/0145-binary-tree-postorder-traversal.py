# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder_st = []
        postorder_ll = []
        temp = root
        postorder_st.append(temp)
        if root is None:
            return postorder_ll 
        while postorder_st : 
            temp = postorder_st.pop()
            postorder_ll.append(temp.val)
            if temp.left:
                postorder_st.append(temp.left)
            if temp.right:
                postorder_st.append(temp.right)
        return postorder_ll[::-1]
        