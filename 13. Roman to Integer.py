class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X':10 , 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        sums = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                sums += symbols[s[i]]
                break
            if symbols[s[i]] < symbols[s[i+1]]:
                sums += symbols[s[i+1]] - symbols[s[i]]
                i += 2
            else:
                sums += symbols[s[i]]
                i += 1
        return sums