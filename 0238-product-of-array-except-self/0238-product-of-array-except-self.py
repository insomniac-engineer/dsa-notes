class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1 2 3 4]

        # prefix
        # [1  1  2 6]

        # postfix
        # [24 12 4 1]

        # result
        # [1*24 12*1 4*2 6*1]
        # [24 12 8 6]

        prefixList = []
        prefixList.append(1)

        postfixList = []
        postfixList.append(1)

        for idx in range(len(nums)):
            print(idx)
            prefixList.append(nums[idx] * prefixList[idx])
        prefixList.pop()

        nums.reverse()
        # [4 3 2 1]
        for idx in range(len(nums)):
            postfixList.append(nums[idx] * postfixList[idx])
            # [1 4 12 24 *]
        postfixList.pop()
        postfixList.reverse()
        print(prefixList)
        print(postfixList)
        for idx in range(len(prefixList)):
            prefixList[idx] *= postfixList[idx]
        return prefixList
