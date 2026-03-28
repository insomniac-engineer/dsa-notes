class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        result = []
        start_range = nums[0]
        current, next = 0, 1

        while next < len(nums):
            if nums[next] - nums[current] != 1:
                if start_range == nums[current]:
                    result.append(f"{start_range}")
                else:
                    result.append(f"{start_range}->{nums[current]}")
                start_range = nums[next]
            current += 1
            next += 1

        if start_range == nums[-1]:
            result.append(f"{start_range}")
        else:
            result.append(f"{start_range}->{nums[-1]}")
        return result




        