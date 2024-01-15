class Solution:
    def isValid(self, s: str) -> bool:
        items = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in items:
                stack.append(i)
            elif not stack or i != items[stack[-1]]:
                return False
            else: 
                stack.pop()
        return stack == []