class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we focus only on frequency of each char
       return Counter(s) == Counter(t)

        