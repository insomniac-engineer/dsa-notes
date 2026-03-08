class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [number] -> index
        # check if map has target - currentNumber in
        key_value = {}
        for idx, n in enumerate(nums):
            if target - n in key_value:
                return [idx, key_value[target - n]]
            key_value[n] = idx
        return []