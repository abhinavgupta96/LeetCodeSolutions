import heapq

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        min_heap = []
        marked = set()
        score = 0

        # Build the min-heap with (value, index) tuples
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
        
        # Process elements from the heap
        while min_heap:
            value, index = heapq.heappop(min_heap)
            
            # Skip if the current index is already marked
            if index in marked:
                continue
            
            # Add the value to the score
            score += value
            
            # Mark the current element and its adjacent ones
            marked.add(index)
            if index > 0:
                marked.add(index - 1)
            if index < n - 1:
                marked.add(index + 1)
        
        return score
