class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        lengths = []
        numbers = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if prev + 1 == nums[i]:
                numbers += 1
            elif prev == nums[i]:
                pass
            else:
                lengths.append(numbers)
                numbers = 1
            prev = nums[i]
        
        lengths.append(numbers)
        return max(lengths)
        