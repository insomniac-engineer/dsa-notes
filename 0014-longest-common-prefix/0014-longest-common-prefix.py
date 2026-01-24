class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #1. Find the shortest world in the strings list
        #2. Each string should have same symbol at each position to match common prefix
        minLenStr = strs[0] # choose the first word by default
        for str in strs:
            if len(str) < len(minLenStr):
                minLenStr = str
        i = 0
        while i < len(minLenStr): # traverse through each char of minLenStr
            for str in strs: # traverse through each word in the string list
                if str[i] != minLenStr[i]: # if character doesn't match - return prefix
                    return str[:i]   
            i += 1
        return str[:i] 