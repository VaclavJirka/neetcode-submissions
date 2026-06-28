class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_temperatures = len(temperatures)
        res = [0] * len_temperatures
        stack = []
        for i in range(len_temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((temperatures[i],i))
        return res
        