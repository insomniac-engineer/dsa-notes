class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str (len(i))
            res += '#'
            res += i
            # "4neet"
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # "12codelovemode"
            length = int(s[i:j]) #12
            start = j + 1 # 'c'
            end = start + length # 'e'

            res.append(s[start:end])

            i = end
        return res
