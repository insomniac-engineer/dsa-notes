class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)
        current = newInterval

        # 1. add all intervals before newInterval
        while i < n and intervals[i][1] < current[0]:
            merged.append(intervals[i])
            i += 1

        # 2. overlapping intervals check
        while i < n and intervals[i][0] <= current[1]:
            current[0] = min(current[0], intervals[i][0])
            current[1] = max(current[1], intervals[i][1])
            i += 1

        # 3. insert overlapped interval 1 time
        merged.append(current)

        # 4. add all remaining non-overlapping intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged