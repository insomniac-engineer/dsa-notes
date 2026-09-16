class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        res = 0
        for t in tokens:
            # IMPORTANT: -3 is not a digit in python, 3 is
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                if t == "+":
                    res = stack.pop() + stack.pop()
                # IMPORTANT: for - and / order plays role
                elif t == "-":
                    temp = stack.pop()
                    res = stack.pop() - temp
                elif t == "*":
                    res = stack.pop() * stack.pop()
                elif t == "/":
                    temp = stack.pop()
                    res = stack.pop() / temp
                stack.append(int(res))
        return stack[-1]