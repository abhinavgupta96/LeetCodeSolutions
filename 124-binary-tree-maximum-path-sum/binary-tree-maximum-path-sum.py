# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(node):
            nonlocal result
            if not node:
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))
            result = max(result, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        
        return result