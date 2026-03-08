class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       key_frequency = {}
       l, r = 0, 0
       res = 0
       while r < len(s):
            while s[r] in key_frequency:
                del key_frequency[s[l]]
                l += 1

            key_frequency[s[r]] = 1
            res = max(res, r - l + 1)
            r += 1

       return res