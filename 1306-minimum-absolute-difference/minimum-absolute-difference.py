class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float("inf")
        result = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            minDiff = min(diff, minDiff)
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minDiff:
                result.append([arr[i-1], arr[i]])
        return result
        