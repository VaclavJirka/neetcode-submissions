class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in nums_set:
                long = 1
                next_n = 1
                while i + next_n in nums_set:
                    long += 1
                    next_n += 1
                longest = max(long, longest)
        return longest
                
        