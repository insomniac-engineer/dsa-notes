class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= end:  # overlap
                end = max(end, cur_end)
            else:
                result.append([start, end])
                start, end = cur_start, cur_end

        result.append([start, end])
        return result