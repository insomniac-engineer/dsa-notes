class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()

        for idx, i in enumerate(nums):
            if target - i in my_dict:
                return [my_dict.get(target - i), idx]
            else:
                my_dict[i] = idx
        return []