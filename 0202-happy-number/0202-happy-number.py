class Solution:
    def isHappy(self, n: int) -> bool:
        # 19 % 10 to get 9
        # 19 //10 to get 1
        seen_numbers = set()
        current_sum = 0
        while n != 1:
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
            current_sum = 0
            while n > 0:
                digit = n % 10
                current_sum += digit * digit
                n //= 10
            n = current_sum
        return True
        