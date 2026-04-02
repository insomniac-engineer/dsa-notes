class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort all points
        points.sort(key=lambda x: x[1])
        counter = 0
        i = 0
        while i < len(points):
            shot = points[i][1]
            while (
                i + 1 < len(points)
                and points[i + 1][0] <= shot
                and shot <= points[i + 1][1]
            ):
                i += 1
            counter += 1
            i += 1
        return counter
