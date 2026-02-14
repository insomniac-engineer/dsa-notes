class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        if len(s) == len(t):
            return t == s
        subsequence = ""
        fullString = ""
        subsequence = s
        fullString = t
        
        i_subsequence = 0
        j_fullString = 0

        while j_fullString < len(fullString) and i_subsequence < len(subsequence):
            if i_subsequence == len(subsequence):
                return True
            if subsequence[i_subsequence] == fullString[j_fullString]:
                print(i_subsequence)
                i_subsequence += 1
                j_fullString +=1
            else:
                j_fullString += 1
        print(i_subsequence)
        return i_subsequence == len(subsequence)

        