class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        previous_value = 0
        #XII = X+I+I
        #IX = X - I
        result = 0
        for char in range(len(s)-1,-1,-1):
            current_char = s[char]
            current_value = symbol_value.get(current_char)

            if previous_value > current_value:
                result -= current_value
            else:
                result += current_value
            previous_value = current_value

        return result