class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum() -> checks if all the characters in a given string are alphanumeric
        # we compare ONLY lower case letters and numbers (alpanumeric), rest - we skip
        left, right = 0, len(s) - 1

        while left <= right:
            if not s[right].isalnum():
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                right -= 1
                left += 1
        return True

