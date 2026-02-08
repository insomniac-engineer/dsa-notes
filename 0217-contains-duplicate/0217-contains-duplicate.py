class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A: sort (elements become adjacent) and compare neighbours elements
        # B: create set and compare length of nums and new set (extra memory)
        # C: create dict and check if value is added only 1 time (contains)

        #A
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
