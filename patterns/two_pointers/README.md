# Two Pointers

Two-pointer techniques use **two index variables** to traverse data structures efficiently.
The key distinction is **pointer responsibility**:

| Sub-Pattern | Pointer Roles | Direction | Typical Signal |
|:------------|:-------------|:----------|:---------------|
| [Read / Write Compression](read_write_compression.md) | One reads, one writes | Same direction (→→) | Remove, Filter, Deduplicate, In-place |
| [Classic Two Pointers](classic_two_pointers.md) | Both explore | Opposite directions (←→) or reverse (←←) | Sorted, Target Sum, Palindrome, Merge |

### Key insight

Two pointers are not about "two indexes".
They are about **separating responsibilities**:
one pointer reads, another defines what is valid — or both converge toward a solution from different ends.
