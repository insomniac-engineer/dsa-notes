class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["bat"] -> ["bat"]
        # ["tea"] -> ["tea", "ate", "nat"]
        # ...
        key_to_words = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            key_to_words.setdefault(sorted_s, []).append(s)
        print(list(key_to_words.values()))
        return list(key_to_words.values())