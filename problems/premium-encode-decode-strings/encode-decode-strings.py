class Solution:
    # TC: O(N)
    # SC: O(N + M)
    # Important! pattern : 5#Hello; digit before #, otherwise parsing would be hell

    # TC: O(N)
    def encode(self, strs: List[str]) -> str:
        parts = []

        # for s in strs:
        #     encoded_string += str(len(s)) + "#"  + s
        # Important! += creates new string

        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)
        # 51#Hello5#World
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0

        while i < len(s):
            while s[j] != "#":
                j += 1
            step = int(s[i:j])
            j += 1
            word = s[j : j + step]
            j = j + step
            i = j
            res.append(word)

        return res
