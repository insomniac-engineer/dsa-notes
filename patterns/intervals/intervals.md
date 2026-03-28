# Intervals

Problems with intervals mostly require ransforming or merging ranges based on specific conditions.

---

## 228. Merge Intervals

Link: <https://leetcode.com/problems/summary-ranges/>
Time Complexity: O(n)
Space Complexity: O(n)

Input: a sorted unique array nums
Output: sorted list of ranges that cover all number in an array

E.g. nums = [0, 1, 2, 4, 5, 7]

result = ["0->2", "4-5", "7"]

> !Important: notice that, for example, value 1 can be checked as **nums[0] + 1 (it's 0 + 1 = 1)** because the array is already sorted asc. Our goal is to cover all ranges that has +1 difference
> To return result as list of str, you can use f-format strings.

Since the array is sorted, we can use a **sliding** index to find the end of each continious sequence. A sequence breakes as soon as nums[i+1] != nums[i] + 1.

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return [] #base case
        i = 0
        result = []

        while i < len(nums):
            startRange = nums[i]

            #range expanding, difference 1
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1

            #the difference is more than 1, we need to update result
            #check if range was expanded at all
            if startRange == nums[i]:
                result.append(f"{startRange}")
            else:
                result.append(f"{startRange}->{nums[i]}")
            
            i+= 1
        return result
```
