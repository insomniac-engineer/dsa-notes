class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # amp each character frequency of magazine, e.g. ['a'] -> 2
        # traverse through ransomNote and check if char of ransomNote exists in map
        # if yes - decrease frueqency character from magazine

        char_freq = {}

        for char in magazine:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for char in ransomNote:
            if char_freq.get(char, 0) <= 0:
                return False
            char_freq[char] -= 1

        return True