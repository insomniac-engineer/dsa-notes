class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort() #[1,1,2,3]

        # slowP = 0
        # fastP = 1

        # while fastP < len(nums):
        #     if nums[slowP] == nums[fastP]:
        #         return True
        #     else:
        #         slowP += 1
        #         fastP += 1
        # return False

        # number_frequency = Counter(nums)
        # for n in number_frequency.values():
        #     if n != 1: return True
        # return False

        # return len(nums) != len(set(nums))

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False