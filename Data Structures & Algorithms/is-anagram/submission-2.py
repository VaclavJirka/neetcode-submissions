class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                ch_index = t.index(i)
                t = t[:ch_index] + t[ch_index+1:]
            else:
                return False
        if len(t) == 0:
            return True
        else:
            return False
        