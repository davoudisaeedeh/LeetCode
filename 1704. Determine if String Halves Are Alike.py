class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()

        a = [i for i in s[:int(len(s) // 2)] if i in vowels]
        b = [i for i in s[int(len(s) // 2):] if i in vowels]

        if len(a) == len(b):
            return True
        else:
            return False