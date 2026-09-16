class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Space Complexity: O(n)
        # Time Complexity: O(n)

        # Pattern: Monotonic stack
        # We can add only lower value on the top of stack
        # If the value is bigger than exisiting in stack we have to update result array with the substraction (current_index - stack_top_value_index)

        stack = []
        # Prefill the result array with 0s, as if we don't find any bigger value in the future, we will return 0
        res = [0] * len(temperatures)

        for idx, i in enumerate(temperatures):
            while stack and i > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = idx - prev_index
            # Append indexes, not values!
            stack.append(idx)
        return res