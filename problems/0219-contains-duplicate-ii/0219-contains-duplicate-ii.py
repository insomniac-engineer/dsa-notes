class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #HashMap + Last Seen Index
        last_seen={}

        for i, n in enumerate(nums):

            if n in last_seen and i - last_seen[n] <= k:
                return True
            last_seen[n] = i
        return False