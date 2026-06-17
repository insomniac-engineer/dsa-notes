class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my_dict = defaultdict(int)
        # for n in nums:
        #     my_dict[n] += 1
        my_dict = Counter(nums)
        # O(NlogK)
        return heapq.nlargest(k, my_dict.keys(), key = my_dict.get)