class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 'e' -> 'a'
        # 'g' -> 'd'

        # 'f' -> 'b'
        # '1' -> '2'
        # '1'
        
        # f13 and b21
        # 'f' -> 'b'
        # '1' -> '2'
        # '3' -> '1'


        s_t = {}

        i = 0

        while i < len(s):
            if s[i] in s_t and s_t[s[i]] != t[i]:
                return False
            else:
                if t[i] in s_t.values() and s[i] not in s_t: return False
                s_t[s[i]] = t[i]
            i += 1
        return True