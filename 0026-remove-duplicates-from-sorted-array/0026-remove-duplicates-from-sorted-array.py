class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        resultIndex = 0

        for i in nums[1:]:
            if i != nums[resultIndex]:
                resultIndex += 1
                nums[resultIndex] = i
        return resultIndex + 1
        