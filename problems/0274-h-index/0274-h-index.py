class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # [0,1,3,5,6]
        #  5 4 3 2 1

        citations.sort()
        startH = 1

        for c in reversed(citations):
            if c >= startH:
                startH +=1
            else: break

        return startH - 1
        