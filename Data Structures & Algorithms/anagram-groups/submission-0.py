class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            s_i = str(sorted(i))
            h_list = hash_map.get(s_i, [])
            h_list.append(i)
            hash_map[s_i] = h_list

        res = []
        for i in hash_map:
            res.append(hash_map[i])
        return res


        