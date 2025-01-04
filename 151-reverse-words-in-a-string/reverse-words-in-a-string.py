class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(l, start, end):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start+=1
                end-=1
        chars = list(s.strip())
        n = len(chars)

        reverse(chars, 0, n-1)
        start = 0
        for end in range(n):
            if chars[end]== " ":
                reverse(chars, start, end-1)
                start = end+1
        reverse(chars, start, n-1)

        result = []
        i = 0
        while i < n: 
            if chars[i]!= " " :
                result.append(chars[i])
            elif result and result[-1]!= " ":
                result.append(chars[i])
            i+=1
        return "".join(result)
        


