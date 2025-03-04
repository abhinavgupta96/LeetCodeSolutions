class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        onesToLeft = [0]*(len(s)+1)
        zeroesToRight = [0]*(len(s)+1)

        minimumFlips = float('inf')

        # Populate the ones_to_left array by counting the number of 1s to the left of each position
        for i in range(1, len(s)+1):
            onesToLeft[i] = onesToLeft[i-1] + (1 if s[i-1]=='1' else 0)

        # Populate the zeros_to_right array by counting the number of 0s to the right of each position
        for i in range(len(s)-1, -1, -1):
            zeroesToRight[i] = zeroesToRight[i+1] + (1 if s[i]=='0' else 0)

        for i in range(len(s)+1):
            minimumFlips = min(minimumFlips, zeroesToRight[i]+onesToLeft[i])
        
        return minimumFlips 