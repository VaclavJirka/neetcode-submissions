class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            w_list = [0] * 26
            for j in i:
                w_list[ord(j)-ord("a")] += 1
            t_w = tuple(w_list)
            l_hash = hash_map.get(t_w, [])
            l_hash.append(i)
            hash_map[t_w] = l_hash

        return list(hash_map.values())


        