class Solution:
    def maxArea(self, height: List[int]) -> int:
        # container is formed by x axis - width and y axis - height
        left, right = 0, len(height) - 1
        max_area = 0

        # Invariant:
        # We always keep the best area seen so far
        # and move the pointer that limits the height
        while left < right:
            # Width is the distance between pointers
            width = right - left

            # Height is limited by the shorter wall
            current_height = min(height[left], height[right])

            area = width * current_height
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
