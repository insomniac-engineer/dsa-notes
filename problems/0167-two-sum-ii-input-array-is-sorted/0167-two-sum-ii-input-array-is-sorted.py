class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  l  r  r  r
        # [2,7,11,15]

        # The array is sorted, which means if I move pointers inward I can adjust the sum in a predictable way.
        # I’ll place one pointer at the beginning and one at the end and compute their sum.
        # If the sum is too small, I need a larger value, so I move the left pointer right.
        # If the sum is too large, I move the right pointer left to decrease it.
        
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                left += 1