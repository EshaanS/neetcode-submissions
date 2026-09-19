class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        res = 0
        max_freq = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            max_freq = max(max_freq, window[s[r]])
            while (r - l + 1) - max_freq > k:
                window[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res