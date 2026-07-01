class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]

        #prefix 1[1, 2, 6, 12]
        #postfix [24,24,12,4]1

        #we want to optimize using prefix and postfix

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # [1, 1, 2, 6]
        print(res)
        postfix = 1

        for j in range (len(nums)-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res

