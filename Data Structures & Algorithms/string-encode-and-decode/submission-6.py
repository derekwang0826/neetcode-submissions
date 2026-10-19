class Solution:

    def encode(self, strs: List[str]) -> str:
        word = []
        for i in strs:
           word.append(str(len(i)))
           word.append("#")
           word.append(i)
        return "".join(word)
    def decode(self, s: str) -> List[str]:
        # str = "5#derek4#wang"
        # sol vid said no state vars? temp ok?
        strs = []
        i = 0
        while i < len(s):
            #must start w/ len#
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return strs