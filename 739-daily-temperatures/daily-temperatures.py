class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previousIndex = stack.pop()
                ans[previousIndex] = index - previousIndex
            stack.append(index)
        return ans