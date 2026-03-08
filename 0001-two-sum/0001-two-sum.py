class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_value = {}
        for idx, n in enumerate(nums):
            if target - n in key_value:
                return [idx, key_value[target - n]]
            key_value[n] = idx
        return []