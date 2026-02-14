class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through t with a pointer and try to match characters from s
        # every time there is a matching character -> advance the pointer in s
        # If all characters of s are consumed, then it’s a subsequence
        p_s = 0
        p_t = 0

        while p_t < len(t) and p_s < len(s):
            if s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1

        return p_s == len(s)
