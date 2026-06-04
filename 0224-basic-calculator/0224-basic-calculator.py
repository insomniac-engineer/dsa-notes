class Solution:
    def calculate(self, s: str) -> int:
        # Hints

        # 1. To represent digit 123, we can use current_number += current_number * 10 + next_digit
        # e.g. current_number = (current_number * 10) + next_digit
        # 2. Keep sign variable, sign = 0 (if +) and sign = -1 (if -)

        current_pos = 0
        sign = 1
        result = []
        stack = []
        while current_pos < len(s):
            if s[current_pos] == "+" or s[current_pos] == "-":
                if s[current_pos] == "+":
                    sign = 1
                else:
                    sign = -1
                current_pos += 1

            elif s[current_pos].isdigit():
                current_number = 0
                while current_pos < len(s) and s[current_pos].isdigit():
                    current_number = current_number * 10 + int(s[current_pos])
                    current_pos += 1
                result.append(current_number * sign)

            #TODO: come back and re-implement this logic
            elif s[current_pos] == "(":
                stack.append(result)
                stack.append(sign)
                result = []
                sign = 1
                current_pos += 1

            elif s[current_pos] == ")":
                evaluated_inner_sum = sum(result)
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result
                result.append(evaluated_inner_sum * prev_sign)
                current_pos += 1

            else: # " "
                current_pos += 1
        return sum(result)