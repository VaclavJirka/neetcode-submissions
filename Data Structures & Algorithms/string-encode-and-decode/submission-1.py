class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += str(len(i)) + "#" + i
        return string

    def decode(self, s: str) -> List[str]:
        reading = False
        counter = 0
        number = ""
        word = ""
        strings = []
        for i in range(len(s)):
            if reading == False and s[i].isnumeric():
                number += s[i]
            if s[i] == "#" and len(number) > 0:
                counter = int(number)
                number = ""
                reading = True
                if counter == 0:
                    strings.append("")
                    reading = False
                continue
            if reading == True and counter > 0:
                word += s[i]
                counter -= 1
                if counter == 0:
                    reading = False
                    strings.append(word)
                    word = ""
        return strings
