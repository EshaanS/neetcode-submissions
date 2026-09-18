class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for num in nums:
            if num not in count_nums:
                count_nums[num] = 1
            else:
                count_nums[num] += 1

        n = len(nums) + 1
        buckets = [[] for _ in range(n)]

        for num, freq in count_nums.items():
            buckets[freq].append(num)
        
        top = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top.append(num)
                if len(top) == k:
                    return top
        return top