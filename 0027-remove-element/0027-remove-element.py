class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 #read pointer
        j = 0 #write pointer

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j