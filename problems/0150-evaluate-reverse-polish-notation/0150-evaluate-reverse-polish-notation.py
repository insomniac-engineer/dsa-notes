class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+' or t == '-' or t == '/' or t == '*': # it's a digit
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(b - a)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(int(b / a))
            else:
                 stack.append(int(t))
        if len(stack) != 0:
            return stack.pop()
        return None