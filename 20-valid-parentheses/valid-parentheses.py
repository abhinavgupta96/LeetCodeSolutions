class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [")","]","}"]
        closing = set(closing)

        for i in s:
            if i not in closing:
                stack.append(i)
            else:
                if not stack:
                    return False
                char = stack.pop()
                if i == "]" and char !="[":
                    return False
                if i == ")" and char !="(":
                    return False
                if i == "}" and char !="{":
                    return False
        return not stack