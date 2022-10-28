class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
        def helper(left, right):
            if left < right:
                s[left],s[right] = s[right],s[left]
                helper(left+1,right-1)
        n = len(s)
        helper(0,n-1)
        return s
        