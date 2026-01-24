class Solution:
    def reverseWords(self, s: str) -> str:
        #1. Traverse through str, add words to list
        #1.1 Each word should be considered as sequence of chars without spaces
        #2. Traverse backwards through list and construct string by adding " " between words
        list_words = []
        current_word = ""
        for char in s:
            if char != ' ':
                current_word += char
            elif current_word != "":
                list_words.append(current_word)
                current_word = ""
                
        if current_word != "":
            list_words.append(current_word)
        result = ""

        for str in list_words[::-1]:
            result += str
            result += " "
        result = result[:-1]
        return result

