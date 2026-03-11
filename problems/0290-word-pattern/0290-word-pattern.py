class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #bijection problem

        #char-word, one-to-one

        words = s.split()
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):

            if c in char_to_word and char_to_word[c] != w:
                return False

            if w in word_to_char and word_to_char[w] != c:
                return False

            char_to_word[c] = w
            word_to_char[w] = c
            
        return True