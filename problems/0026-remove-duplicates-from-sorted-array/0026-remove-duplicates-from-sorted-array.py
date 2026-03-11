class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowP = 0
        fastP = 1

        while fastP < len(nums):
            if nums[slowP] != nums[fastP]:
                slowP += 1
                nums[slowP] = nums[fastP]
            fastP += 1
        return slowP + 1
