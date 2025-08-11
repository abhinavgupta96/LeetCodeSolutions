class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        charMapping = {" " : " "}
        nextIndex = 0

        for c in key:
            if c not in charMapping:
                charMapping[c] = ascii_lowercase[nextIndex]
                nextIndex+=1
        
        decoded_message = "".join(charMapping[char] for char in message)
        return decoded_message
