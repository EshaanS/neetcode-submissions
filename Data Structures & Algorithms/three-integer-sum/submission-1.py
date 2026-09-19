class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        final = []
        seen = []
        for i in range(0, len(nums)):
            target = nums_sort[i]
            if target not in seen:
                seen.append(target)
                l = i + 1
                r = len(nums) - 1
                result = []
                while l < r:
                    sum = nums_sort[l] + nums_sort[r]
                    if sum + target > 0:
                        r -= 1
                    elif sum + target < 0:
                        l += 1
                    else:
                        result = [nums_sort[l], nums_sort[r], target]
                        final.append(result)
                        l += 1
                        while l < r and nums_sort[l] == nums_sort[l - 1]:
                            l += 1
        return final