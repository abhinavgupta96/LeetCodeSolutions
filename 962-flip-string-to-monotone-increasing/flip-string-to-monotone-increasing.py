class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips_to_zero = 0
        flips_to_one = 0

        # Iterate through each character in the string.
        for char in s:
            if char == '0':
                # If the current character is '0':
                # - flips_to_zero remains the same because '0' can stay '0'.
                # - flips_to_one needs to be incremented because '1' needs to be flipped to '0'.
                flips_to_one = min(flips_to_zero, flips_to_one) + 1
            else:
                # If the current character is '1':
                # - flips_to_zero needs to be incremented because '0' needs to be flipped to '1'.
                # - flips_to_one remains the same because '1' can stay '1'.
                flips_to_one = min(flips_to_zero, flips_to_one)
                flips_to_zero += 1

        # The result is the minimum number of flips needed to make the entire string monotone increasing.
        return min(flips_to_zero, flips_to_one)