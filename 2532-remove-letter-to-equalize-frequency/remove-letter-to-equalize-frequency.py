class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        
        # Step 2: Iterate through each character and try removing it
        for char in word:
            # Reduce the count of the current character by 1
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]  # Remove the character if its frequency is 0
            
            # Check if all frequencies are the same
            if len(set(freq.values())) == 1:
                return True
            
            # Restore the character count for the next iteration
            freq[char] += 1
        
        # If no valid removal was found
        return False
        