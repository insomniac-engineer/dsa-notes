class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort approach

        # nums.sort()
        # i = 0

        # while i < len(nums):
        #     if i + 1 != len(nums):
        #         if nums[i] == nums[i+1]: 
        #             return True
        #     i += 1
        # return False
        
        # Set

        my_set = set()

        for i in nums:
            if i in my_set: return True
            else:
                my_set.add(i)
        return False