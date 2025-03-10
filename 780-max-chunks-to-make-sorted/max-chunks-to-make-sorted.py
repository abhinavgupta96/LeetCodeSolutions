class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        maxValue = 0
        chunkCount = 0

        for i, num in enumerate(arr):
            maxValue = max(maxValue, arr[i])
            if i == maxValue:
                chunkCount+=1
        
        return chunkCount