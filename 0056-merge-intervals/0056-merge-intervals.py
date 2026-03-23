class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        slow_pointer = 0
        result = []

        startPosition = intervals[slow_pointer][0]
        current_end = intervals[slow_pointer][1]

        for fast_p in range(1, len(intervals)):
            if current_end >= intervals[fast_p][0]:
                # расширяем текущий интервал
                current_end = max(current_end, intervals[fast_p][1])
                slow_pointer += 1
            else:
                result.append([startPosition, current_end])
                startPosition = intervals[fast_p][0]
                current_end = intervals[fast_p][1]
                slow_pointer += 1

        result.append([startPosition, current_end])
        return result