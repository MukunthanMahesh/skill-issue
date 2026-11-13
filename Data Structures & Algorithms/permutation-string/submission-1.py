from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq1 = defaultdict(int)
        for c in s1:
            freq1[c] += 1
        print(freq1)
        print('x')

        l, r = 0, len(s1)
        while r < len(s2) + 1:
            freq2 = defaultdict(int)
            for c in s2[l:r]:
                freq2[c] += 1
            print(freq2)
            if freq1 == freq2:
                return True
            r += 1
            l += 1
        return False
