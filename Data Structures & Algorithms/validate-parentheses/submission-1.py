class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {'(' : ')', '{' : '}', '[' : ']' }

        stack = []
        for c in s:
            if stack and stack[-1] in pair and c == pair[stack[-1]]:
                stack.pop()
            else:
                stack.append(c)
 
        if stack == []:
            return True
        else:
            return False

        