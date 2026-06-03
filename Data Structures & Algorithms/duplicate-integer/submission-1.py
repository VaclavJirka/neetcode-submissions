class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_nums = []
        for i in nums:
            if i in list_nums:
                return True
            else: list_nums.append(i)
        return False
        