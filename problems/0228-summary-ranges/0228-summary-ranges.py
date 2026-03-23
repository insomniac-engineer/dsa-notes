class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0

        while i < len(nums):
            # fix the start position
            start = nums[i]
            
            # move while next value == +1
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            # if we didn't make a move aka there is no value with value+1
            if start == nums[i]:
                result.append(f"{start}")
            else: # if we moved and found the sequence values
                result.append(f"{start}->{nums[i]}")
            
            i += 1
        
        return result