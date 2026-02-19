class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        res = []

        nums = sorted(nums)
        i = 0
        while i < len(nums) - 2:
            if i != 0:
                if nums[i] == nums[i-1]:
                    i += 1
                    continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[right] + nums[left] == target:
                    res.append([nums[i], nums[right], nums[left]])
                    right -= 1
                    left += 1
                    # Skip intervals on right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                    # Skip intervals on left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif nums[right] + nums[left] > target:
                    right -=1
                else:
                    left += 1
            i += 1

        return res