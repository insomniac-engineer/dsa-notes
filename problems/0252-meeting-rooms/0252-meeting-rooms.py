class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        # 1. Sort by start time since we're looking for overlaps
        intervals.sort()

        # IMPORTANT - See how last element check is elegantly handled by len(intervals) - 1
        for i in range(len(intervals) - 1):
            # Meeting overlaps if start time of next meeting is less than end time of current one
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
