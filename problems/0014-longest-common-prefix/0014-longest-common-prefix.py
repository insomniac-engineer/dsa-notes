class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)):
            for s in strs:
                print(s)
                if i == len(s) or s[i] != first_word[i]:
                    return first_word[:i]
        return first_word
