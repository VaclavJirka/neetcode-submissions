class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            number = 1
            for j in range(len(nums)):
                if not j == i:
                    number = number * nums[j]
            res.append(number)
        return res