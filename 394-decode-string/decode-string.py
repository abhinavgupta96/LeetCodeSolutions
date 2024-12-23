class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1]!="[":
                    substr = stack.pop() + substr
                # below pop removes the opening bracket
                stack.pop() 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                k = int(k)
                stack.append(k*substr)
        return "".join(stack)
        