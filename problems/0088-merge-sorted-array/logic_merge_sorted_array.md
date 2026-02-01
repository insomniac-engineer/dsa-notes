# Problem Analysis: Merge Sorted Array (88)

## 🍀 Intuition

Use 2 pointers technique but **backwards**.
The main problem is that **all elements** from nums2 are merged into nums1 and it's done **in-place**.

## 🎯 Key Idea / Pattern

**Two Pointers (From the End / Reverse Pointers)**.

We use three pointers:

* `i`: Index of the last element of `nums1` (`m - 1`).
* `j`: Index of the last element of `nums2` (`n - 1`).
* `k`: Index of the current insertion point in `nums1` (`m + n - 1`).

The time complexity is $O(m + n)$ because we only iterate through the total number of elements once. The space complexity is $O(1)$ as the merge is done in place.

## 🧠 Common mistakes

1. **The Tail:** Forgetting to handle the edge case where there's `nums2 tail` requiring us to explicitly copy the remaining elements from `nums2` into the front of `nums1`.
    E.g:
    Input: [5,6,7,0,0,0]
    [1,2,3]

    After nums1 is traversed [0,0,0,5,6,7], but there's remaining tail of [1,2,3].

## 💻 Code (Python)

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1 #read pointer
        j = n - 1 #read pointer
        k = m + n - 1 #write in-place pointer

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j-=1
            else:
                nums1[k] = nums1[i]
                i-=1
            k-=1
        while j >= 0: #write remaining tail
            nums1[k] = nums2[j]
            j-=1
            k-=1