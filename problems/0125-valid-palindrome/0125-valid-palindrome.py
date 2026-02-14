class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filteredString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # # swap approach, instead of the swap we compare

        # left,right = 0, len(filteredString) - 1

        # while (left < right):
        #     if filteredString[left] != filteredString[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # it's actually quite hard to remember the regex, so we can do it in one pass

        # isalnum() -> checks if all the characters in a given string are alphanumeric
        # we compare ONLY lower case letters and numbers (alphanumeric), rest - we skip

        # Complexity: O(n) time, O(1) space (if we ignore the input string)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
