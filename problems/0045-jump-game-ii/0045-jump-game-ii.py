class Solution:
    def jump(self, nums: List[int]) -> int:
        furthestPoint = 0
        steps = 0
        endPoint = 0

        for i in range(len(nums) - 1):
            furthestPoint = max(furthestPoint, i + nums[i])
            if endPoint == i:
                steps += 1
                endPoint = furthestPoint
        return steps
