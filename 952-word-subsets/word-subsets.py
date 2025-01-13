class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()

        for word in words2:
            freq = Counter(word)
            for char, count in freq.items():
                max_freq[char] = max(max_freq[char], count)
        result = []
        for word in words1:
            freq = Counter(word)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        return result