class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle: return 0

        i = 0
        j = 0
        startIndex = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] != needle[j]:
                j = 0
                startIndex += 1
                i = startIndex
            else:
                i += 1
                j += 1
            if j == len(needle):
                return startIndex
        return -1