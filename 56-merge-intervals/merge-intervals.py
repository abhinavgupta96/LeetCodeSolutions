class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_list = [intervals[0]]

        for interval in intervals:
            if merged_list[-1][1] < interval[0]:
                merged_list.append(interval)
            else:
                merged_list[-1][1] = max(merged_list[-1][1], interval[1])
        return merged_list
        