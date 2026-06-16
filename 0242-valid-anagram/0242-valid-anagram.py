class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
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