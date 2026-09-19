class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                start = num
                current_length = 1
                while start + 1 in set_nums:
                    current_length += 1
                    start += 1
                longest = max(longest, current_length)
        return longest  