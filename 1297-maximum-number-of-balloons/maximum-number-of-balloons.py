class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = Counter(text)

        charCount['o'] //=2
        charCount['l'] //=2

        return min(charCount[char] for char in 'balon')