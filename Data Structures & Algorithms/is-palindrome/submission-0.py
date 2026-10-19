class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_word = s.lower().replace(" ", "")
        for i in lower_word:
            if i.isalnum():
                pass
            else:
                lower_word = lower_word.replace(i, "")
        reverse = lower_word[::-1]
        if lower_word == reverse:
            return True
        return False