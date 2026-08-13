class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'}': '{', ']':'[', ')':'('}

        stack = []

        for c in s: 
            if c == '}' or c == ']' or c == ')':
                if stack and stack[-1] != mp[c] or not stack:                            
                    return False
                elif stack: 
                    stack.pop()
            else:
                stack.append(c)

        return not stack 


        