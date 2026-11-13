from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0 
        char_map = defaultdict(int)

        while r < len(s):
            char_map[s[r]] += 1
            if (r - l + 1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            
