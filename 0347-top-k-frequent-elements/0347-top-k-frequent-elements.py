class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Space Complexity: O(n log k)
        
        my_dict = Counter(nums)

        heap = []

        for val, freq in my_dict.items():
            heapq.heappush(heap, (freq, val))
            # Time Complexity: O(n log k)
            if len(heap) > k:
                heapq.heappop(heap)

        return [val for _, val in heap]