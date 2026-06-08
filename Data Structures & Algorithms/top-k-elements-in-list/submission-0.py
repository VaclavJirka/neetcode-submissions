class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            val = hash_map.get(i, 0) + 1
            hash_map[i] = val
        values = hash_map.items()
        values = sorted(values, key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(values[i][0])
        return res


        
        