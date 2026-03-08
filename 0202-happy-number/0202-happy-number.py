class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)
        
            total = 0
            while n:
                digit = n % 10 #9
                total += digit * digit # pow of 2 for 9
                n //= 10 # 1
            n = total # 82
        return True