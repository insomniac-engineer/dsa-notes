class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # mantain key-value pairs [char] -> string

        # Invariants:
        # if key(char) exists in map and maps to different string -> false
        # if value(string) exists in seen_string set and maps to different char -> false
        
        # [a] -> dog
        # FALSE: [a] -> cat
        # FALSE: [c] -> dog

        seen_set = set()
        char_to_word = {}
        i = 0
        j = 0
        while i < len(pattern):
            if j >= len(s):
                return False
            word = ""
            while j < len(s) and s[j] != " ":
                word += s[j]
                j += 1
            if word in seen_set and pattern[i] not in char_to_word:
                return False #word was already mapped previously [c] -> dog, but we added [b] -> dog
            if pattern[i] not in char_to_word:
                char_to_word[pattern[i]] = word
            elif char_to_word[pattern[i]] != word:
                return False
            seen_set.add(word)
            i += 1
            j += 1
        return j >= len(s)