class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O (n * k logk)
        # Time Space: O (n * k)


        # creates empty list value if key doesn't exist (KeyError)
        my_dict = defaultdict(list)

        for s in strs:
            # key in hash table MUST be hashable (immutable)
            # when we sort string it returns list (mutable)
            
            sorted_s = tuple(sorted(s))
            # alternative: sorted_s = ('').join(sorted(s))
            my_dict[sorted_s].append(s)
        return list (my_dict.values())
