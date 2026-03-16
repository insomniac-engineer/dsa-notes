class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #slow and fast pointer approach
        slow = 0
        fast = 1
        result = []

        startIndex = 0
        
        while fast < len(nums):
            if nums[slow] + 1 != nums[fast]:
                if nums[slow] - 1 != nums[slow - 1]:
                    result.append(f"{nums[slow]}")
                else:
                    result.append(f"{nums[startIndex]}->{nums[slow]}")
                startIndex = slow + 1
            slow += 1
            fast += 1
        
        if startIndex != len(nums):
            if nums[startIndex] == nums[fast - 1]:
                result.append(f"{nums[startIndex]}")
            else:
                result.append(f"{nums[startIndex]}->{nums[fast - 1]}")
        return result

        