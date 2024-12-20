class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ms = float("inf")
        result = []
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < ms:
                ms = diff
                result = [[arr[i-1], arr[i]]]
            elif diff==ms:
                result.append([arr[i-1], arr[i]])        
        return result