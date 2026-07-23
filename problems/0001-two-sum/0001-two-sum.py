class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Space Complexity: O(n)
        # Time Complexity: O(n)
        
        val_index = dict()
        for idx, val in enumerate(nums):
            if (target - val) in val_index:
                return [idx, val_index[target - val]]
            val_index[val] = idx
        return []
