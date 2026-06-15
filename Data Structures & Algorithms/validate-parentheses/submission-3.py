class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(", "[", "{"}
        closing = {"(":")", "[":"]","{":"}"}
        brackets = []
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i in opening:
                brackets.append(i)
            else:
                if len(brackets) == 0:
                    return False
                if closing[brackets[-1]] != i:
                    return False
                brackets.pop()
        if len(brackets) == 0:
            return True
        return False
        