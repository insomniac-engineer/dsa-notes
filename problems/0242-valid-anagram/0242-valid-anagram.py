class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #    A: sort both strings, traverse through them and if s[i] != t[i] return False
        #    B: use HashMap and compare added values
        #       In Pythonic way: return Counter(s) == Counter(t)
        #    C: use HashMap and compare subtracted values
        if len(s) != len(t): return False
        
        key_value = dict()

        for i in s:
            if i in key_value:
                key_value[i] = key_value.get(i) + 1
            else:
                key_value[i] = 1

        for j in t:
            if j not in key_value:
                return False
            elif key_value[j] <= 0:
                return False
            key_value[j] = key_value.get(j) - 1
        return True