class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Helper function to calculate the power of x
        def getPower(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps

        # Create a list of tuples: (power, number)
        nums_with_power = [(getPower(x), x) for x in range(lo, hi + 1)]

        # Sort by power value, and by number if power values are equal
        nums_with_power.sort(key=lambda pair: (pair[0], pair[1]))

        # Return the k-th element's number (1-based index, so k-1)
        return nums_with_power[k - 1][1]

        