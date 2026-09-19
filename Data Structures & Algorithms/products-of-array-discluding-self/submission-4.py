class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for i in range(1, len(nums)):
            result.append(result[i - 1] * nums[i - 1])

        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            result[i] = result[i] * product

        return result