class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # we have children appetite array
        # g = [1,2,3]
        # we have available cookies sizes
        # s = [1,1]

        # invariant is that size of the cookies is equal/more than child's apetite
        # s[j] >= g[i]

        # if yes: we move to next child and move to next cooking
        # if no: we move to next cookie

        #IMPORANT! both lists should be sorted
        g.sort()
        s.sort()
        total = 0
        current_cookie_index = 0
        current_child_apetite_index = 0
        while current_cookie_index < len(s) and current_child_apetite_index < len(g):
            if g[current_child_apetite_index] <= s[current_cookie_index]: #invariant current apetite should be satisfied by size of cookie
                total += 1
                current_child_apetite_index += 1
            current_cookie_index += 1
        return total