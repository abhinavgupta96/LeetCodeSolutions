class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        for c in s:
            if c in hashmap : ##this checks if c is in key of the dict, ie c is a closing bracket
                if stack and stack[-1]==hashmap[c]: ##check if stack is not empty and the last element in the stack is the corresponding opening bracket for c
                    stack.pop() #if so pop the open bracket from stack
                else:
                    return False
            else:
                stack.append(c) #if c is a open bracket append to the stack
        if stack: #if item exists in stack, then string was not balanced
            return False
        else:
            return True
        