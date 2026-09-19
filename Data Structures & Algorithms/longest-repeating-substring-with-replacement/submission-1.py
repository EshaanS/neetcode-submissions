class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 1
            else:
                window[s[r]] += 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            res = max(sum(window.values()), res)
        return res