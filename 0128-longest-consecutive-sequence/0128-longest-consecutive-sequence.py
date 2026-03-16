class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        existing_values = set(nums)
        longest_seq = 0

        for i in existing_values:
            # check if it's the first element in sequence
            if i - 1 not in existing_values: #True if it's the first element
                length = 0
                while (i + length) in existing_values:
                    length += 1
                longest_seq = max(longest_seq, length)
        return longest_seq
                