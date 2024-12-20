class Solution:
    def isValid(self, s: str) -> bool:
        closing = [")", "]", "}"]

        stack = []
        for i in s:
            if i not in closing:
                stack.append(i)
            else:
                if not stack:
                    return False
                char = stack.pop()
                if char =="{" and i!="}":
                    return False
                if char =="(" and i!=")":
                    return False
                if char =="[" and i!="]":
                    return False
        return not stack