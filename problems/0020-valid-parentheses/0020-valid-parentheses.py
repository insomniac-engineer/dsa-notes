class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if len(s) == 1: return False
        stack = []

        brackets = {'(':')', '{': '}', '[': ']'}

        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            elif len(stack) == 0 or b != stack.pop():
                return False
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(']')
            elif  s[i] == '{':
                stack.append('}')
            elif  s[i] == '(':
                stack.append(')')
            else:
                if len(stack) == 0 or s[i] != stack.pop():
                    return False
            i += 1
        return len(stack) == 0