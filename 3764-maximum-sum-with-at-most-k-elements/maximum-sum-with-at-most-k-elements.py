import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        minHeap = []

        for i in range(len(grid)):
            row = sorted(grid[i], reverse=True)
            for num in row[:limits[i]]:
                heapq.heappush(minHeap, num)
                if len(minHeap) > k:
                    heapq.heappop(minHeap)
        return sum(minHeap)