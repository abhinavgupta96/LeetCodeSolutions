class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        result = 0
        #Brute Force
        # for i in range(len(arr)):
        #     minVal = arr[i]
        #     for j in range(i,len(arr)):
        #         minVal = min(minVal, arr[j])
        #         result = (result + minVal)% MOD
        # return result
        prevElement = [-1]*len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            prevElement[i] = stack[-1] if stack else -1
            stack.append(i)
        
        nextElement = [len(arr)]*len(arr)
        stack = []

        for i in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            nextElement[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        
        for i in range(len(arr)):
            left = i - prevElement[i]
            right = nextElement[i] - i
            result += arr[i] * left * right
            result = result % MOD

        return result