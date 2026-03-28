pattern: Intervals


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        i = 0

        while i < len(nums):
            start = nums[i]

            # all the numbers go in order + 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            # format string in case with start has changed or not (if there is any range)
            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(f"{start}")
            i += 1

        return result
