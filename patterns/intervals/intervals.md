# Intervals

Problems with intervals mostly require transforming or merging ranges based on specific conditions.

Typical probles: meetings rooms, calendar schedule, task overlap, non-overlapping intervals

Overview: https://www.hellointerview.com/learn/code/intervals/overview

## Sorting

Intervals ALWAYS require **sorting**.

* sort by **start** to detect overlaps

> If the start of next meeting < end of previous one = overlap

* sort by **end** to maximize *non-overlapping* intervals

---

### 228. Summary Ranges (sorted by start)

Link: <https://leetcode.com/problems/summary-ranges/>
Time Complexity: O(n)
Space Complexity: O(n)

Input: a sorted (ascending) unique array nums
Output: sorted list of ranges that cover all number in an array

E.g. nums = [0, 1, 2, 4, 5, 7]

result = ["0->2", "4->5", "7"]

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

### 252. Meeting Rooms (sorted by start)

Link: https://www.hellointerview.com/learn/code/intervals/can-attend-meetings (LC needs premium)

Task:

Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

intervals = [(1,5),(3,9),(6,8)]
false
Explanation: The meetings (1,5) and (3,9) overlap.

> Meeting overlaps if start time of meeting is less than end time of previous one

```python
    class Solution
        def canAttendMeetings(self, intervals: List[List[int]] -> bool):
            #1. Sort by start time since we're looking for overlaps
            intervals.sort()
            # IMPORTANT - See how last element check is elegantly handled by len(intervals) - 1
            for i in range(len(intervals) - 1):
                if intervals[i][1] > intervals[i+1][0]:
                    return False
            return True
```

### 452. Minimum number of arrows to burst ballons (sort by end)

    [------- Balloon А (Longest) -------]        [1, 8]
        [ B ]                                [3, 4]
                [ C ]                        [5, 6]

If we **sort by end**, we would just need 2 arrows:

B destroys A and itself
C destroys itself

If we sort by start, we need 3:

A is the longest one, but doesn't destroy smaller B and C
B destroys itself
C destroys itself

To sort by end:

```python
points.sort(key=lambda x:x[1])

```