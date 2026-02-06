class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #    return Counter(s) == Counter(t)

        # we focus on char frequency, so we need key-value DS, where key is char and value is how frequent we meet it
        # once we traverse through s, we can traverse through t and check:
        # if t[i] is in map - substract value from map
        # if not - return false

        if len(s) != len(t): return False #anagram frequency should be the same for both strings; base case
        frequency_char_map = {}
        for i in s:
            frequency_char_map[i] = frequency_char_map.get(i,0) + 1 #get existing value and increment or put 0

        for i in t:
            if i not in frequency_char_map or frequency_char_map[i] == 0:
                return False
            frequency_char_map[i] -=1
        return True

        

        