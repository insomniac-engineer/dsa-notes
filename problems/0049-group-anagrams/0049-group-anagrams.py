class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if i ask for a key that doesn't exist - return []
        my_dict = defaultdict(list)

        for s in strs:
            # we cant use sorted(s) because it returns list (mutable)
            # list can't be stored as key in dict
            # extra memory allocation
            #sorted_s = ('').join(sorted(s))
            sorted_s = tuple(sorted(s))
            my_dict[sorted_s].append(s)
        return list (my_dict.values())